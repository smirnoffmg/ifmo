// toc nodes to be inserted 
var tocTab = new Array();
var ir=0;

tocTab[ir++] = new Array ("Top", "Содержание", "contents.htm");
tocTab[ir++] = new Array ("1", "Шифрование", "theory.htm");
tocTab[ir++] = new Array ("1.1", "Классификация шифров", "class.htm");
tocTab[ir++] = new Array ("1.2", "Методы замены", "sr.htm");
tocTab[ir++] = new Array ("1.3", "Криптоанализ", "anal.htm");
tocTab[ir++] = new Array ("1.4", "Пример", "example.htm");
tocTab[ir++] = new Array ("1.5", "Термины", "termins.htm");

tocTab[ir++] = new Array ("2", 	"Мануал", "manual.htm");
tocTab[ir++] = new Array ("2.1", "Главное окно", "wMain.htm");
tocTab[ir++] = new Array ("2.1.1", "Меню", "wMain_Menu.htm");
tocTab[ir++] = new Array ("2.1.2", "Инструменты", "wMain_ToolBar.htm");

tocTab[ir++] = new Array ("2.2", "Шифротекст", "wCode.htm");
tocTab[ir++] = new Array ("2.3", "Алфавит", "wAlph.htm");
tocTab[ir++] = new Array ("2.4", "Открытый текст", "wDeCode.htm");
tocTab[ir++] = new Array ("2.5", "График", "wGraph.htm");
tocTab[ir++] = new Array ("2.6", "Биграммы", "wDbl.htm");
tocTab[ir++] = new Array ("2.7", "Информация", "wInfo.htm");
tocTab[ir++] = new Array ("2.8", "Фраза", "wFind.htm");

tocTab[ir++] = new Array ("3", "Разработчики", "authors.htm");

var nCols = 4;
var showNumbers = true;
var backColor = "#FF9900";
var normalColor = "#FFFFFF";
var lastVisitColor = "#FFFF80";
var currentColor = "#000000";
var titleColor = "#FFFFFF";



var mLevel = 1;                 // number of levels minus 1 the headlines of which are presentet with large and bold fonts   
var textSizes = new Array(1, 0.7, 0.6, 0.7, 0.6);           // font-size factors for: [0] the title "Table of Contents", [1] larger and bold fonts [2] smaller fonts if MS Internet Explorer [3] larger and bold fonts [4] smaller fonts if Netscape Navigator.
var fontTitle = "Helvetica,Arial"; // font-family of the title "Table of Contents"
var fontLines = "Helvetica,Arial"; // font-family of the headlines
var tocScroll=true;             // Automatic scrolling of the ToC frame (true) or not(false)
var tocBehaviour = new Array(1,0); // Indicates how the ToC shall change when clicking in the heading symbol (1st arg.) resp. in the heading text (2nd arg). Arg's meaning: 0 = No change, 1 = ToC changes with automatic collapsing, 2 = ToC changes with no automatic collapsing.
var tocLinks = new Array(1,0);  // Indicates wether the content's location shall be changed when clicking in the heading symbol (1st arg.) resp. in the heading text (2nd arg). Arg's meaning: 1 = No, 0 = Yes. 
	
/*------------------------------------------------------------------- 
Author's Statement:
This script is based on ideas of the author.
You may copy, modify and use it for any purpose. The only condition is that if you publish web pages that use this script you point to its author at a suitable place and don't remove this Statement from it.
It's your responsibility to handle possible bugs even if you didn't modify anything. I cannot promise any support.
Dieter Bungers
GMD (www.gmd.de) and infovation (www.infovation.de)
--------------------------------------------------------------------*/
// Checking the client's browser and setting the text sizes of the headings in the ToC depending on the global parameter textSizes set in tocParas and the browser useed:

var isIE = navigator.appName.toLowerCase().indexOf("explorer") > -1;
var mdi = (isIE) ? textSizes[1]:textSizes[3];
var sml = (isIE) ? textSizes[2]:textSizes[4];

// Other global variables:

// oldCurrentNumber is required to keep a hedings ordering string (or number) in case the ToC should change (tocChange > 0) but the content's location should remain unchanged (i.e. noLink == 1). In those cases the heading preceeded by oldCurrentNumber has to remain hilited (otherwise the heading preceeded by currentNumber has to be hilited).
var oldCurrentNumber = "", oldLastVisitNumber = "";

// toDisplay: Array to keep the display status for each heading. It is initialised so only the top level headings are displayed (headings preceeded by a single string without a dot):  
var toDisplay = new Array();
for (ir=0; ir<tocTab.length; ir++) {
	toDisplay[ir] = tocTab[ir][0].split(".").length==1;
}

// ***************************************
// The function redisplays the ToC and the content 
// ***************************************

function reDisplay(currentNumber,tocChange,noLink,e) {
// Input parameters:
// currentNumber: Hierarchical ordering string (or number) of the heading the user wants to display (we call this heading the "current"). This controls the change of both, the ToC depending on the second parameter tocChange and the content's URL depending on the third parameter noLink. 
// tocChange: Controls how to change the ToC. 0 = No change, 1 = Change with automatic collapsing of expanded headings that are not on the path to the current heading, 2 = Change wthout automatic colapsing (as use for example by Windows Explorer or Mac OS).
// noLink: Controls wether the content's URL shall be changed to the value given by the 3rd element of an tocTab's entry (= 0) or not (= 1).
// e: The event that triggered the function call. If it is set it must be the event object.

// If there is an event that triggered the function call: Checking the control key depending on the browser used. If it is pressed and tocChange is greater than 0 tocChange is set to 2 so the ToC schanges without automatic collapsing: 
	if (e) {
		ctrlKeyDown = (isIE) ? e.ctrlKey : (e.modifiers==2);
		if (tocChange && ctrlKeyDown) tocChange = 2;
	}

// Initializing the ToC window's document and displaying the title on it's top. The ToC is performed by a HTML table:
	toc.document.clear();
	toc.document.write("<html>\n<head>\n<title>ToC</title>\n</head>\n<body bgcolor=\"" + backColor + "\">\n<table border=0 cellspacing=1 cellpadding=0>\n<tr>\n<td colspan=" + (nCols+1) + "><a href=\"javaScript:history.go(0)\" onMouseDown=\"parent.reDisplay('" + tocTab[0][0] + "',0,0)\" style=\"font-family: " + fontTitle + "; font-weight:bold; font-size:" + textSizes[0] + "em; color: " + titleColor + "; text-decoration:none\">" + tocTab[0][1] + "</a></td></tr>\n<tr>");

// This is for defining the number of columns of the ToC table and the width of the last one. The first cells of each following row shall be empty or contain the heading symbol, the last ones are reserved for displaying the heding's text:
	for (k=0; k<nCols; k++) {
		toc.document.write("<td>&nbsp;</td>");
	}
	toc.document.write("<td width=240>&nbsp;</td></tr>");

//	currentLevel = the level of the current heading:
	var currentNumArray = currentNumber.split(".");
	var currentLevel = currentNumArray.length-1;

// currentIndex = Current heading's index in the tocTab array:
	var currentIndex = null;
	for (i=0; i<tocTab.length; i++) {
		if (tocTab[i][0] == currentNumber) {
			currentIndex = i;
			break;
		}
	}
// If currentNumber was not found in tocTab: No action.
	if (currentIndex == null) return false;
	
// currentIsExpanded = Expand/Collaps-state of the current heading:
	if (currentIndex < tocTab.length-1) {
		nextLevel = tocTab[currentIndex+1][0].split(".").length-1;
		currentIsExpanded = nextLevel > currentLevel && toDisplay[currentIndex+1];
	} 
	else currentIsExpanded = false;

// Determining the new URL and target (if given) of the current heading
	theHref = (noLink) ? "" : tocTab[currentIndex][2];
	theTarget = tocTab[currentIndex][3];

// ***************************************
// 1st loop over the tocTab entries: Determining which heading to display:
// ***************************************
	for (i=1; i<tocTab.length; i++) {

// Nothing to do if the tocChange parameter is set to 0. If it is set to 1 or 2...
		if (tocChange) {
			thisNumber = tocTab[i][0];
			thisNumArray = thisNumber.split(".");
			thisLevel = thisNumArray.length-1;
// isOnPath = this heading is on the path to the current heading in the ToC hierarchy or a sibling of such a heading:
			isOnPath = true;
			if (thisLevel > 0) {
				for (j=0; j<thisLevel; j++) {
					isOnPath = (j>currentLevel) ? false : isOnPath && (thisNumArray[j] == currentNumArray[j]);
				}
			} 
// By the following, the headings on the path to the current heading and the siblings of such  headings (isOnPath==true, see above) will be displayed anyway. If the tocChange parameter is set to 1 no other heading will be displayed. If it is set to a number greater than 1 the headings that have been displayed before will additionally be displayed again.  
			toDisplay[i] = (tocChange == 1) ? isOnPath : (isOnPath || toDisplay[i]);

// Now let's perform the expand/collaps mechanism: If the heading is a descendant of the current heading it's next display depends on wether the current heading was expanded or collapsed. If it was expanded the descendants have not to be displayed this time, otherwise only the childs has to be displayed but not the grandchildren, great-grandchildren etc.. Remember that currentIsExpanded says wether the current heading was expanded or not. The if-clause is a criteria for being a descendant of the current heading. If it's a descendant and thisLevel == currentLevel+1 it's a child.
			if (thisNumber.indexOf(currentNumber+".")==0 && thisLevel > currentLevel) { 		
				if (currentIsExpanded) toDisplay[i] = false;
				else toDisplay[i] = (thisLevel == currentLevel+1); 
			}
		} 
	} // End of loop over the tocTab

// ***************************************
// 2nd loop over the tocTab entries: Displaying the headings:
// ***************************************
	var scrollY=0, addScroll=tocScroll; 
	for (i=1; i<tocTab.length; i++) {
		if (toDisplay[i]) {
			thisNumber = tocTab[i][0];
			thisNumArray = thisNumber.split(".");
			thisLevel = thisNumArray.length-1;
			isCurrent = (i == currentIndex);

// Setting the heading's symbol depending on whether this heading is expanded or not or if it is a leaf. It is expanded if the next heading has a greater level than this one AND has to be displayed: 
			if (i < tocTab.length-1) {
				nextLevel = tocTab[i+1][0].split(".").length-1;
				img = (thisLevel >= nextLevel) ? "leaf" : ((toDisplay[i+1]) ? "minus" : "plus");
			} 
			else img = "leaf"; // The last heading is always a leaf.

// If the scoll parameter is set true than increment the scrollY value:
			if (addScroll) scrollY+=((thisLevel<2)?mdi:sml)*25;
			if (isCurrent) addScroll=false;

// thisTextColor = the text color of this heading
			if (noLink)
				thisTextColor = (thisNumber==oldCurrentNumber) ? currentColor:((thisNumber==oldLastVisitNumber) ? lastVisitColor:normalColor);
			else thisTextColor = (thisNumber==currentNumber) ? currentColor:((thisNumber==oldCurrentNumber) ? lastVisitColor:normalColor);

// Now writing this ToC line, i.e. a table row...:			
			toc.document.writeln("<tr>");

// ...first some empty cells for the line indent depending on the level of this heading...:
			for (k=1; k<=thisLevel; k++) {
				toc.document.writeln("<td>&nbsp;</td>");
			}

// ...then the hading symbol and the heading text each with a javaScript link caling just this function reDisplay again: 
			toc.document.writeln("<td valign=top><a href=\"javaScript:history.go(0)\" onMouseDown=\"parent.reDisplay('" + thisNumber + "'," + tocBehaviour[0] + "," + tocLinks[0] + ",event)\"><img src=\"img/" + img + ".gif\" width=13 height=12 border=0></a></td> <td colspan=" + (nCols-thisLevel) + "><a href=\"javaScript:history.go(0)\" onMouseDown=\"parent.reDisplay('" + thisNumber + "'," + tocBehaviour[1] + "," + tocLinks[1] + ",event)\" style=\"font-family: " + fontLines + ";" + ((thisLevel<=mLevel)?"font-weight:bold":"") +  "; font-size:" + ((thisLevel<=mLevel)?mdi:sml) + "em; color: " + thisTextColor + "; text-decoration:none\">" + ((showNumbers)?(thisNumber+" "):"") + tocTab[i][1] + "</a></td></tr>");
		}
	} // End of loop over the tocTab

// ***************************************
// Closing the ToC document, scrolling its frame window and displaying new content in the content frame or in the top window if required 
// ***************************************

// Updating the global variables oldCurrentNumber and oldLastVisitNumber. See above for its definition
	if (!noLink) { 
		oldLastVisitNumber = oldCurrentNumber;
		oldCurrentNumber = currentNumber;
	}

// Closing the ToC table and the document
	toc.document.writeln("</table>\n</body></html>");
	toc.document.close();

// Scrolling the ToC if required
	if (tocScroll) toc.scroll(0,scrollY);
	
// Setting the top or content window's location if required
	if (theHref) 
		if (theTarget=="top") top.location.href = theHref;
		else if (theTarget=="parent") parent.location.href = theHref;
		else if (theTarget=="blank") open(theHref,"");
		else content.location.href = theHref;
}
