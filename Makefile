clean: clean_latex clean_vscode


clean_latex:
	find . -type f -iname "*.out" -delete
	find . -type f -iname "*aux" -delete
	find . -type f -iname "*bbl" -delete
	find . -type f -iname "*blg" -delete
	find . -type f -iname "*log" -delete
	find . -type f -iname "*toc" -delete
	find . -type f -iname "*.ptb" -delete
	find . -type f -iname "*.tod" -delete
	find . -type f -iname "*.fls" -delete
	find . -type f -iname "*.fdb_latexmk" -delete
	find . -type f -iname "*.lof" -delete
	find . -type f -iname "*.pdf" -delete

clean_vscode:
	find . -type d -iname ".vscode" -exec rm -rf "{}" \;
