--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO cvetomaster;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO cvetomaster;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO cvetomaster;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO cvetomaster;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO cvetomaster;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO cvetomaster;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO cvetomaster;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO cvetomaster;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO cvetomaster;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO cvetomaster;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO cvetomaster;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO cvetomaster;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: basket_basket; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.basket_basket (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    session character varying(255) NOT NULL
);


ALTER TABLE public.basket_basket OWNER TO cvetomaster;

--
-- Name: basket_basketitem; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.basket_basketitem (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    object_id uuid NOT NULL,
    price double precision,
    title character varying(255),
    quantity integer NOT NULL,
    basket_id uuid NOT NULL,
    color_id uuid,
    content_type_id integer NOT NULL,
    CONSTRAINT basket_basketitem_quantity_check CHECK ((quantity >= 0))
);


ALTER TABLE public.basket_basketitem OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquet (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    slug character varying(50),
    content text,
    price integer NOT NULL,
    discount_price integer NOT NULL,
    favourite boolean NOT NULL,
    discount boolean NOT NULL,
    meta_keywords character varying(255),
    meta_description character varying(255),
    width integer NOT NULL,
    height integer NOT NULL,
    weight integer NOT NULL,
    show_in_recommended_block boolean NOT NULL,
    promo_text character varying(255),
    block integer,
    "order" integer NOT NULL,
    meta_title character varying(255) NOT NULL,
    CONSTRAINT bouquets_bouquet_height_check CHECK ((height >= 0)),
    CONSTRAINT bouquets_bouquet_order_check CHECK (("order" >= 0)),
    CONSTRAINT bouquets_bouquet_weight_check CHECK ((weight >= 0)),
    CONSTRAINT bouquets_bouquet_width_check CHECK ((width >= 0))
);


ALTER TABLE public.bouquets_bouquet OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_colors; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquet_colors (
    id integer NOT NULL,
    bouquet_id uuid NOT NULL,
    bouquetcolor_id uuid NOT NULL
);


ALTER TABLE public.bouquets_bouquet_colors OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_colors_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.bouquets_bouquet_colors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bouquets_bouquet_colors_id_seq OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_colors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.bouquets_bouquet_colors_id_seq OWNED BY public.bouquets_bouquet_colors.id;


--
-- Name: bouquets_bouquet_flowers; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquet_flowers (
    id integer NOT NULL,
    bouquet_id uuid NOT NULL,
    flower_id uuid NOT NULL
);


ALTER TABLE public.bouquets_bouquet_flowers OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_flowers_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.bouquets_bouquet_flowers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bouquets_bouquet_flowers_id_seq OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_flowers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.bouquets_bouquet_flowers_id_seq OWNED BY public.bouquets_bouquet_flowers.id;


--
-- Name: bouquets_bouquet_photos; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquet_photos (
    id integer NOT NULL,
    bouquet_id uuid NOT NULL,
    bouquetphoto_id uuid NOT NULL,
    sort_value integer NOT NULL
);


ALTER TABLE public.bouquets_bouquet_photos OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_photos_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.bouquets_bouquet_photos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bouquets_bouquet_photos_id_seq OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_photos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.bouquets_bouquet_photos_id_seq OWNED BY public.bouquets_bouquet_photos.id;


--
-- Name: bouquets_bouquet_types; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquet_types (
    id integer NOT NULL,
    bouquet_id uuid NOT NULL,
    bouquettype_id uuid NOT NULL
);


ALTER TABLE public.bouquets_bouquet_types OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_types_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.bouquets_bouquet_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bouquets_bouquet_types_id_seq OWNER TO cvetomaster;

--
-- Name: bouquets_bouquet_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.bouquets_bouquet_types_id_seq OWNED BY public.bouquets_bouquet_types.id;


--
-- Name: bouquets_bouquetcolor; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquetcolor (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    uses_in_filters boolean NOT NULL,
    "order" integer NOT NULL,
    title character varying(255) NOT NULL,
    color character varying(7) NOT NULL,
    CONSTRAINT bouquets_bouquetcolor_order_check CHECK (("order" >= 0))
);


ALTER TABLE public.bouquets_bouquetcolor OWNER TO cvetomaster;

--
-- Name: bouquets_bouquetphoto; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquetphoto (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    image character varying(100) NOT NULL,
    alt_title character varying(255) NOT NULL
);


ALTER TABLE public.bouquets_bouquetphoto OWNER TO cvetomaster;

--
-- Name: bouquets_bouquettype; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_bouquettype (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    uses_in_filters boolean NOT NULL,
    "order" integer NOT NULL,
    title character varying(255) NOT NULL,
    description text,
    CONSTRAINT bouquets_bouquettype_order_check CHECK (("order" >= 0))
);


ALTER TABLE public.bouquets_bouquettype OWNER TO cvetomaster;

--
-- Name: bouquets_pricecategory; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.bouquets_pricecategory (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    uses_in_filters boolean NOT NULL,
    "order" integer NOT NULL,
    title character varying(255) NOT NULL,
    price_from integer,
    price_to integer,
    CONSTRAINT bouquets_pricecategory_order_check CHECK (("order" >= 0)),
    CONSTRAINT bouquets_pricecategory_price_from_check CHECK ((price_from >= 0)),
    CONSTRAINT bouquets_pricecategory_price_to_check CHECK ((price_to >= 0))
);


ALTER TABLE public.bouquets_pricecategory OWNER TO cvetomaster;

--
-- Name: crm_crmfile; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.crm_crmfile (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    file character varying(100) NOT NULL
);


ALTER TABLE public.crm_crmfile OWNER TO cvetomaster;

--
-- Name: customers_customer; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.customers_customer (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    name character varying(255) NOT NULL,
    phone character varying(255) NOT NULL,
    email character varying(254) NOT NULL,
    address text NOT NULL,
    orders_as_sender integer NOT NULL,
    orders_as_receiver integer NOT NULL,
    CONSTRAINT customers_customer_orders_as_receiver_check CHECK ((orders_as_receiver >= 0)),
    CONSTRAINT customers_customer_orders_as_sender_check CHECK ((orders_as_sender >= 0))
);


ALTER TABLE public.customers_customer OWNER TO cvetomaster;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO cvetomaster;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO cvetomaster;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO cvetomaster;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO cvetomaster;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO cvetomaster;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO cvetomaster;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO cvetomaster;

--
-- Name: finance_coupon; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.finance_coupon (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    active boolean NOT NULL,
    value integer NOT NULL,
    code character varying(30) NOT NULL,
    valid_until timestamp with time zone,
    max_redemptions integer,
    times_redeemed integer NOT NULL,
    CONSTRAINT finance_coupon_max_redemptions_check CHECK ((max_redemptions >= 0)),
    CONSTRAINT finance_coupon_times_redeemed_check CHECK ((times_redeemed >= 0))
);


ALTER TABLE public.finance_coupon OWNER TO cvetomaster;

--
-- Name: finance_financeoperation; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.finance_financeoperation (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    amount double precision NOT NULL,
    type integer NOT NULL,
    order_id uuid,
    CONSTRAINT finance_financeoperation_type_check CHECK ((type >= 0))
);


ALTER TABLE public.finance_financeoperation OWNER TO cvetomaster;

--
-- Name: flowers_flower; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.flowers_flower (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    uses_in_filters boolean NOT NULL,
    "order" integer NOT NULL,
    title character varying(255) NOT NULL,
    color character varying(7) NOT NULL,
    description text,
    image character varying(100),
    CONSTRAINT flowers_flower_order_check CHECK (("order" >= 0))
);


ALTER TABLE public.flowers_flower OWNER TO cvetomaster;

--
-- Name: goods_item; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.goods_item (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    slug character varying(50),
    content text,
    price integer NOT NULL,
    discount_price integer NOT NULL,
    favourite boolean NOT NULL,
    discount boolean NOT NULL,
    meta_keywords character varying(255),
    meta_description character varying(255),
    show_in_additional_goods_block boolean NOT NULL,
    "order" integer NOT NULL,
    meta_title character varying(255) NOT NULL,
    CONSTRAINT goods_item_order_check CHECK (("order" >= 0))
);


ALTER TABLE public.goods_item OWNER TO cvetomaster;

--
-- Name: goods_item_photos; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.goods_item_photos (
    id integer NOT NULL,
    item_id uuid NOT NULL,
    itemphoto_id uuid NOT NULL
);


ALTER TABLE public.goods_item_photos OWNER TO cvetomaster;

--
-- Name: goods_item_photos_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.goods_item_photos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.goods_item_photos_id_seq OWNER TO cvetomaster;

--
-- Name: goods_item_photos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.goods_item_photos_id_seq OWNED BY public.goods_item_photos.id;


--
-- Name: goods_item_types; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.goods_item_types (
    id integer NOT NULL,
    item_id uuid NOT NULL,
    itemtype_id uuid NOT NULL
);


ALTER TABLE public.goods_item_types OWNER TO cvetomaster;

--
-- Name: goods_item_types_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.goods_item_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.goods_item_types_id_seq OWNER TO cvetomaster;

--
-- Name: goods_item_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.goods_item_types_id_seq OWNED BY public.goods_item_types.id;


--
-- Name: goods_itemphoto; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.goods_itemphoto (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    image character varying(100) NOT NULL,
    alt_title character varying(255) NOT NULL
);


ALTER TABLE public.goods_itemphoto OWNER TO cvetomaster;

--
-- Name: goods_itemtype; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.goods_itemtype (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    uses_in_filters boolean NOT NULL,
    "order" integer NOT NULL,
    title character varying(255) NOT NULL,
    description text,
    it_is_card boolean NOT NULL,
    CONSTRAINT goods_itemtype_order_check CHECK (("order" >= 0))
);


ALTER TABLE public.goods_itemtype OWNER TO cvetomaster;

--
-- Name: orders_order; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.orders_order (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    order_id integer NOT NULL,
    status integer NOT NULL,
    is_payed boolean NOT NULL,
    payment_type integer NOT NULL,
    delivery_date date NOT NULL,
    delivery_time_period integer,
    exact_delivery_time time without time zone,
    card_type integer NOT NULL,
    card_text text NOT NULL,
    sender character varying(255) NOT NULL,
    sender_phone character varying(255) NOT NULL,
    sender_email character varying(254) NOT NULL,
    sender_address character varying(255) NOT NULL,
    sender_comment text NOT NULL,
    receiver character varying(255) NOT NULL,
    receiver_phone character varying(255) NOT NULL,
    receiver_email character varying(254) NOT NULL,
    receiver_address character varying(255) NOT NULL,
    receiver_comment text NOT NULL,
    our_comment text NOT NULL,
    basket_id uuid NOT NULL,
    payment_id integer,
    sberbank_order_id character varying(255) NOT NULL,
    promocode character varying(30) NOT NULL,
    promocode_value integer,
    CONSTRAINT orders_order_card_type_check CHECK ((card_type >= 0)),
    CONSTRAINT orders_order_delivery_time_period_check CHECK ((delivery_time_period >= 0))
);


ALTER TABLE public.orders_order OWNER TO cvetomaster;

--
-- Name: pages_feedback; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.pages_feedback (
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    phone character varying(255),
    fio character varying(255),
    email character varying(255),
    text text
);


ALTER TABLE public.pages_feedback OWNER TO cvetomaster;

--
-- Name: thumbnail_kvstore; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.thumbnail_kvstore (
    key character varying(200) NOT NULL,
    value text NOT NULL
);


ALTER TABLE public.thumbnail_kvstore OWNER TO cvetomaster;

--
-- Name: yandex_money_payment; Type: TABLE; Schema: public; Owner: cvetomaster
--

CREATE TABLE public.yandex_money_payment (
    id integer NOT NULL,
    pub_date timestamp with time zone NOT NULL,
    shop_id integer NOT NULL,
    scid integer NOT NULL,
    customer_number character varying(64) NOT NULL,
    order_amount numeric(15,2) NOT NULL,
    article_id integer,
    payment_type character varying(2) NOT NULL,
    order_number character varying(64) NOT NULL,
    cps_email character varying(100),
    cps_phone character varying(15),
    success_url character varying(200) NOT NULL,
    fail_url character varying(200) NOT NULL,
    status character varying(16) NOT NULL,
    invoice_id integer,
    shop_amount numeric(15,2),
    order_currency integer NOT NULL,
    shop_currency integer,
    performed_datetime timestamp with time zone,
    user_id integer,
    CONSTRAINT yandex_money_payment_article_id_check CHECK ((article_id >= 0)),
    CONSTRAINT yandex_money_payment_invoice_id_check CHECK ((invoice_id >= 0)),
    CONSTRAINT yandex_money_payment_order_currency_check CHECK ((order_currency >= 0)),
    CONSTRAINT yandex_money_payment_scid_check CHECK ((scid >= 0)),
    CONSTRAINT yandex_money_payment_shop_currency_check CHECK ((shop_currency >= 0)),
    CONSTRAINT yandex_money_payment_shop_id_check CHECK ((shop_id >= 0))
);


ALTER TABLE public.yandex_money_payment OWNER TO cvetomaster;

--
-- Name: yandex_money_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: cvetomaster
--

CREATE SEQUENCE public.yandex_money_payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yandex_money_payment_id_seq OWNER TO cvetomaster;

--
-- Name: yandex_money_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cvetomaster
--

ALTER SEQUENCE public.yandex_money_payment_id_seq OWNED BY public.yandex_money_payment.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_colors ALTER COLUMN id SET DEFAULT nextval('public.bouquets_bouquet_colors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_flowers ALTER COLUMN id SET DEFAULT nextval('public.bouquets_bouquet_flowers_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_photos ALTER COLUMN id SET DEFAULT nextval('public.bouquets_bouquet_photos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_types ALTER COLUMN id SET DEFAULT nextval('public.bouquets_bouquet_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_photos ALTER COLUMN id SET DEFAULT nextval('public.goods_item_photos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_types ALTER COLUMN id SET DEFAULT nextval('public.goods_item_types_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.yandex_money_payment ALTER COLUMN id SET DEFAULT nextval('public.yandex_money_payment_id_seq'::regclass);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: basket_basket_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.basket_basket
    ADD CONSTRAINT basket_basket_pkey PRIMARY KEY (id);


--
-- Name: basket_basketitem_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.basket_basketitem
    ADD CONSTRAINT basket_basketitem_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquet_colors_bouquet_id_bouquetcolor_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_colors
    ADD CONSTRAINT bouquets_bouquet_colors_bouquet_id_bouquetcolor_id_key UNIQUE (bouquet_id, bouquetcolor_id);


--
-- Name: bouquets_bouquet_colors_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_colors
    ADD CONSTRAINT bouquets_bouquet_colors_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquet_flowers_bouquet_id_flower_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_flowers
    ADD CONSTRAINT bouquets_bouquet_flowers_bouquet_id_flower_id_key UNIQUE (bouquet_id, flower_id);


--
-- Name: bouquets_bouquet_flowers_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_flowers
    ADD CONSTRAINT bouquets_bouquet_flowers_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquet_photos_bouquet_id_bouquetphoto_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_photos
    ADD CONSTRAINT bouquets_bouquet_photos_bouquet_id_bouquetphoto_id_key UNIQUE (bouquet_id, bouquetphoto_id);


--
-- Name: bouquets_bouquet_photos_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_photos
    ADD CONSTRAINT bouquets_bouquet_photos_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquet_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet
    ADD CONSTRAINT bouquets_bouquet_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquet_slug_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet
    ADD CONSTRAINT bouquets_bouquet_slug_key UNIQUE (slug);


--
-- Name: bouquets_bouquet_types_bouquet_id_bouquettype_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_types
    ADD CONSTRAINT bouquets_bouquet_types_bouquet_id_bouquettype_id_key UNIQUE (bouquet_id, bouquettype_id);


--
-- Name: bouquets_bouquet_types_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_types
    ADD CONSTRAINT bouquets_bouquet_types_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquetcolor_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquetcolor
    ADD CONSTRAINT bouquets_bouquetcolor_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquetphoto_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquetphoto
    ADD CONSTRAINT bouquets_bouquetphoto_pkey PRIMARY KEY (id);


--
-- Name: bouquets_bouquettype_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquettype
    ADD CONSTRAINT bouquets_bouquettype_pkey PRIMARY KEY (id);


--
-- Name: bouquets_pricecategory_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_pricecategory
    ADD CONSTRAINT bouquets_pricecategory_pkey PRIMARY KEY (id);


--
-- Name: crm_crmfile_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.crm_crmfile
    ADD CONSTRAINT crm_crmfile_pkey PRIMARY KEY (id);


--
-- Name: customers_customer_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.customers_customer
    ADD CONSTRAINT customers_customer_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: finance_coupon_code_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.finance_coupon
    ADD CONSTRAINT finance_coupon_code_key UNIQUE (code);


--
-- Name: finance_coupon_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.finance_coupon
    ADD CONSTRAINT finance_coupon_pkey PRIMARY KEY (id);


--
-- Name: finance_financeoperation_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.finance_financeoperation
    ADD CONSTRAINT finance_financeoperation_pkey PRIMARY KEY (id);


--
-- Name: flowers_flower_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.flowers_flower
    ADD CONSTRAINT flowers_flower_pkey PRIMARY KEY (id);


--
-- Name: goods_item_photos_item_id_itemphoto_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_photos
    ADD CONSTRAINT goods_item_photos_item_id_itemphoto_id_key UNIQUE (item_id, itemphoto_id);


--
-- Name: goods_item_photos_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_photos
    ADD CONSTRAINT goods_item_photos_pkey PRIMARY KEY (id);


--
-- Name: goods_item_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item
    ADD CONSTRAINT goods_item_pkey PRIMARY KEY (id);


--
-- Name: goods_item_slug_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item
    ADD CONSTRAINT goods_item_slug_key UNIQUE (slug);


--
-- Name: goods_item_types_item_id_itemtype_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_types
    ADD CONSTRAINT goods_item_types_item_id_itemtype_id_key UNIQUE (item_id, itemtype_id);


--
-- Name: goods_item_types_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_types
    ADD CONSTRAINT goods_item_types_pkey PRIMARY KEY (id);


--
-- Name: goods_itemphoto_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_itemphoto
    ADD CONSTRAINT goods_itemphoto_pkey PRIMARY KEY (id);


--
-- Name: goods_itemtype_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_itemtype
    ADD CONSTRAINT goods_itemtype_pkey PRIMARY KEY (id);


--
-- Name: orders_order_basket_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_order_basket_id_key UNIQUE (basket_id);


--
-- Name: orders_order_payment_id_key; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_order_payment_id_key UNIQUE (payment_id);


--
-- Name: orders_order_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_order_pkey PRIMARY KEY (id);


--
-- Name: pages_feedback_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.pages_feedback
    ADD CONSTRAINT pages_feedback_pkey PRIMARY KEY (id);


--
-- Name: thumbnail_kvstore_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.thumbnail_kvstore
    ADD CONSTRAINT thumbnail_kvstore_pkey PRIMARY KEY (key);


--
-- Name: yandex_money_payment_pkey; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.yandex_money_payment
    ADD CONSTRAINT yandex_money_payment_pkey PRIMARY KEY (id);


--
-- Name: yandex_money_payment_shop_id_da801f3894099f6_uniq; Type: CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.yandex_money_payment
    ADD CONSTRAINT yandex_money_payment_shop_id_da801f3894099f6_uniq UNIQUE (shop_id, order_number);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_group_permissions_0e939a4f ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_group_permissions_8373b171 ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_permission_417f1b1c ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_user_groups_0e939a4f ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_user_groups_e8701ad4 ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_user_user_permissions_8373b171 ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: basket_basket_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX basket_basket_afd1a1a8 ON public.basket_basket USING btree (updated_at);


--
-- Name: basket_basket_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX basket_basket_fde81f11 ON public.basket_basket USING btree (created_at);


--
-- Name: basket_basketitem_399a0583; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX basket_basketitem_399a0583 ON public.basket_basketitem USING btree (color_id);


--
-- Name: basket_basketitem_417f1b1c; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX basket_basketitem_417f1b1c ON public.basket_basketitem USING btree (content_type_id);


--
-- Name: basket_basketitem_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX basket_basketitem_afd1a1a8 ON public.basket_basketitem USING btree (updated_at);


--
-- Name: basket_basketitem_afdeaea9; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX basket_basketitem_afdeaea9 ON public.basket_basketitem USING btree (basket_id);


--
-- Name: basket_basketitem_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX basket_basketitem_fde81f11 ON public.basket_basketitem USING btree (created_at);


--
-- Name: bouquets_bouquet_70a17ffa; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_70a17ffa ON public.bouquets_bouquet USING btree ("order");


--
-- Name: bouquets_bouquet_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_afd1a1a8 ON public.bouquets_bouquet USING btree (updated_at);


--
-- Name: bouquets_bouquet_colors_b7dda7b0; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_colors_b7dda7b0 ON public.bouquets_bouquet_colors USING btree (bouquet_id);


--
-- Name: bouquets_bouquet_colors_ea5deffc; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_colors_ea5deffc ON public.bouquets_bouquet_colors USING btree (bouquetcolor_id);


--
-- Name: bouquets_bouquet_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_fde81f11 ON public.bouquets_bouquet USING btree (created_at);


--
-- Name: bouquets_bouquet_flowers_b7dda7b0; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_flowers_b7dda7b0 ON public.bouquets_bouquet_flowers USING btree (bouquet_id);


--
-- Name: bouquets_bouquet_flowers_de08a452; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_flowers_de08a452 ON public.bouquets_bouquet_flowers USING btree (flower_id);


--
-- Name: bouquets_bouquet_photos_b7dda7b0; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_photos_b7dda7b0 ON public.bouquets_bouquet_photos USING btree (bouquet_id);


--
-- Name: bouquets_bouquet_photos_df8c8f9e; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_photos_df8c8f9e ON public.bouquets_bouquet_photos USING btree (bouquetphoto_id);


--
-- Name: bouquets_bouquet_slug_27606868f8c6b900_like; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_slug_27606868f8c6b900_like ON public.bouquets_bouquet USING btree (slug varchar_pattern_ops);


--
-- Name: bouquets_bouquet_types_1a604fa9; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_types_1a604fa9 ON public.bouquets_bouquet_types USING btree (bouquettype_id);


--
-- Name: bouquets_bouquet_types_b7dda7b0; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquet_types_b7dda7b0 ON public.bouquets_bouquet_types USING btree (bouquet_id);


--
-- Name: bouquets_bouquetcolor_70a17ffa; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquetcolor_70a17ffa ON public.bouquets_bouquetcolor USING btree ("order");


--
-- Name: bouquets_bouquetcolor_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquetcolor_afd1a1a8 ON public.bouquets_bouquetcolor USING btree (updated_at);


--
-- Name: bouquets_bouquetcolor_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquetcolor_fde81f11 ON public.bouquets_bouquetcolor USING btree (created_at);


--
-- Name: bouquets_bouquetphoto_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquetphoto_afd1a1a8 ON public.bouquets_bouquetphoto USING btree (updated_at);


--
-- Name: bouquets_bouquetphoto_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquetphoto_fde81f11 ON public.bouquets_bouquetphoto USING btree (created_at);


--
-- Name: bouquets_bouquettype_70a17ffa; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquettype_70a17ffa ON public.bouquets_bouquettype USING btree ("order");


--
-- Name: bouquets_bouquettype_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquettype_afd1a1a8 ON public.bouquets_bouquettype USING btree (updated_at);


--
-- Name: bouquets_bouquettype_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_bouquettype_fde81f11 ON public.bouquets_bouquettype USING btree (created_at);


--
-- Name: bouquets_pricecategory_70a17ffa; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_pricecategory_70a17ffa ON public.bouquets_pricecategory USING btree ("order");


--
-- Name: bouquets_pricecategory_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_pricecategory_afd1a1a8 ON public.bouquets_pricecategory USING btree (updated_at);


--
-- Name: bouquets_pricecategory_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX bouquets_pricecategory_fde81f11 ON public.bouquets_pricecategory USING btree (created_at);


--
-- Name: crm_crmfile_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX crm_crmfile_afd1a1a8 ON public.crm_crmfile USING btree (updated_at);


--
-- Name: crm_crmfile_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX crm_crmfile_fde81f11 ON public.crm_crmfile USING btree (created_at);


--
-- Name: customers_customer_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX customers_customer_afd1a1a8 ON public.customers_customer USING btree (updated_at);


--
-- Name: customers_customer_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX customers_customer_fde81f11 ON public.customers_customer USING btree (created_at);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX django_admin_log_417f1b1c ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX django_admin_log_e8701ad4 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX django_session_de54fa62 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: finance_coupon_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX finance_coupon_afd1a1a8 ON public.finance_coupon USING btree (updated_at);


--
-- Name: finance_coupon_c76a5e84; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX finance_coupon_c76a5e84 ON public.finance_coupon USING btree (active);


--
-- Name: finance_coupon_code_3050700842e48a19_like; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX finance_coupon_code_3050700842e48a19_like ON public.finance_coupon USING btree (code varchar_pattern_ops);


--
-- Name: finance_coupon_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX finance_coupon_fde81f11 ON public.finance_coupon USING btree (created_at);


--
-- Name: finance_financeoperation_69dfcb07; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX finance_financeoperation_69dfcb07 ON public.finance_financeoperation USING btree (order_id);


--
-- Name: finance_financeoperation_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX finance_financeoperation_afd1a1a8 ON public.finance_financeoperation USING btree (updated_at);


--
-- Name: finance_financeoperation_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX finance_financeoperation_fde81f11 ON public.finance_financeoperation USING btree (created_at);


--
-- Name: flowers_flower_70a17ffa; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX flowers_flower_70a17ffa ON public.flowers_flower USING btree ("order");


--
-- Name: flowers_flower_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX flowers_flower_afd1a1a8 ON public.flowers_flower USING btree (updated_at);


--
-- Name: flowers_flower_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX flowers_flower_fde81f11 ON public.flowers_flower USING btree (created_at);


--
-- Name: goods_item_70a17ffa; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_70a17ffa ON public.goods_item USING btree ("order");


--
-- Name: goods_item_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_afd1a1a8 ON public.goods_item USING btree (updated_at);


--
-- Name: goods_item_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_fde81f11 ON public.goods_item USING btree (created_at);


--
-- Name: goods_item_photos_4d6aaba0; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_photos_4d6aaba0 ON public.goods_item_photos USING btree (itemphoto_id);


--
-- Name: goods_item_photos_82bfda79; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_photos_82bfda79 ON public.goods_item_photos USING btree (item_id);


--
-- Name: goods_item_slug_74816f2f4c4b1876_like; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_slug_74816f2f4c4b1876_like ON public.goods_item USING btree (slug varchar_pattern_ops);


--
-- Name: goods_item_types_82bfda79; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_types_82bfda79 ON public.goods_item_types USING btree (item_id);


--
-- Name: goods_item_types_b463ee43; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_item_types_b463ee43 ON public.goods_item_types USING btree (itemtype_id);


--
-- Name: goods_itemphoto_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_itemphoto_afd1a1a8 ON public.goods_itemphoto USING btree (updated_at);


--
-- Name: goods_itemphoto_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_itemphoto_fde81f11 ON public.goods_itemphoto USING btree (created_at);


--
-- Name: goods_itemtype_70a17ffa; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_itemtype_70a17ffa ON public.goods_itemtype USING btree ("order");


--
-- Name: goods_itemtype_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_itemtype_afd1a1a8 ON public.goods_itemtype USING btree (updated_at);


--
-- Name: goods_itemtype_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX goods_itemtype_fde81f11 ON public.goods_itemtype USING btree (created_at);


--
-- Name: orders_order_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX orders_order_afd1a1a8 ON public.orders_order USING btree (updated_at);


--
-- Name: orders_order_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX orders_order_fde81f11 ON public.orders_order USING btree (created_at);


--
-- Name: pages_feedback_afd1a1a8; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX pages_feedback_afd1a1a8 ON public.pages_feedback USING btree (updated_at);


--
-- Name: pages_feedback_fde81f11; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX pages_feedback_fde81f11 ON public.pages_feedback USING btree (created_at);


--
-- Name: thumbnail_kvstore_key_2b995e08553ca215_like; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX thumbnail_kvstore_key_2b995e08553ca215_like ON public.thumbnail_kvstore USING btree (key varchar_pattern_ops);


--
-- Name: yandex_money_payment_e8701ad4; Type: INDEX; Schema: public; Owner: cvetomaster
--

CREATE INDEX yandex_money_payment_e8701ad4 ON public.yandex_money_payment USING btree (user_id);


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bask_content_type_id_1c8e08a3859eb623_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.basket_basketitem
    ADD CONSTRAINT bask_content_type_id_1c8e08a3859eb623_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: basket_ba_color_id_202c41acfadac5f5_fk_bouquets_bouquetcolor_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.basket_basketitem
    ADD CONSTRAINT basket_ba_color_id_202c41acfadac5f5_fk_bouquets_bouquetcolor_id FOREIGN KEY (color_id) REFERENCES public.bouquets_bouquetcolor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: basket_basketite_basket_id_6a5148ebeca1ac7b_fk_basket_basket_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.basket_basketitem
    ADD CONSTRAINT basket_basketite_basket_id_6a5148ebeca1ac7b_fk_basket_basket_id FOREIGN KEY (basket_id) REFERENCES public.basket_basket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bo_bouquetcolor_id_3b67e8d74929d486_fk_bouquets_bouquetcolor_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_colors
    ADD CONSTRAINT bo_bouquetcolor_id_3b67e8d74929d486_fk_bouquets_bouquetcolor_id FOREIGN KEY (bouquetcolor_id) REFERENCES public.bouquets_bouquetcolor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bo_bouquetphoto_id_4023249ebec1246c_fk_bouquets_bouquetphoto_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_photos
    ADD CONSTRAINT bo_bouquetphoto_id_4023249ebec1246c_fk_bouquets_bouquetphoto_id FOREIGN KEY (bouquetphoto_id) REFERENCES public.bouquets_bouquetphoto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bouq_bouquettype_id_4de0f04082fca506_fk_bouquets_bouquettype_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_types
    ADD CONSTRAINT bouq_bouquettype_id_4de0f04082fca506_fk_bouquets_bouquettype_id FOREIGN KEY (bouquettype_id) REFERENCES public.bouquets_bouquettype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bouquets_bou_bouquet_id_198fa2238ceb3685_fk_bouquets_bouquet_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_photos
    ADD CONSTRAINT bouquets_bou_bouquet_id_198fa2238ceb3685_fk_bouquets_bouquet_id FOREIGN KEY (bouquet_id) REFERENCES public.bouquets_bouquet(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bouquets_bou_bouquet_id_697623b4890988c6_fk_bouquets_bouquet_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_types
    ADD CONSTRAINT bouquets_bou_bouquet_id_697623b4890988c6_fk_bouquets_bouquet_id FOREIGN KEY (bouquet_id) REFERENCES public.bouquets_bouquet(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bouquets_bou_bouquet_id_7d7a16901ab85cd2_fk_bouquets_bouquet_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_colors
    ADD CONSTRAINT bouquets_bou_bouquet_id_7d7a16901ab85cd2_fk_bouquets_bouquet_id FOREIGN KEY (bouquet_id) REFERENCES public.bouquets_bouquet(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bouquets_bouq_bouquet_id_1600e2018acd96b_fk_bouquets_bouquet_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_flowers
    ADD CONSTRAINT bouquets_bouq_bouquet_id_1600e2018acd96b_fk_bouquets_bouquet_id FOREIGN KEY (bouquet_id) REFERENCES public.bouquets_bouquet(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bouquets_bouque_flower_id_588ad5b7bda633ec_fk_flowers_flower_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.bouquets_bouquet_flowers
    ADD CONSTRAINT bouquets_bouque_flower_id_588ad5b7bda633ec_fk_flowers_flower_id FOREIGN KEY (flower_id) REFERENCES public.flowers_flower(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: finance_financeope_order_id_28968228f27a7fa9_fk_orders_order_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.finance_financeoperation
    ADD CONSTRAINT finance_financeope_order_id_28968228f27a7fa9_fk_orders_order_id FOREIGN KEY (order_id) REFERENCES public.orders_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: goods_item__itemphoto_id_16a99fc096136333_fk_goods_itemphoto_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_photos
    ADD CONSTRAINT goods_item__itemphoto_id_16a99fc096136333_fk_goods_itemphoto_id FOREIGN KEY (itemphoto_id) REFERENCES public.goods_itemphoto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: goods_item_photos_item_id_3d4790e5024519ea_fk_goods_item_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_photos
    ADD CONSTRAINT goods_item_photos_item_id_3d4790e5024519ea_fk_goods_item_id FOREIGN KEY (item_id) REFERENCES public.goods_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: goods_item_ty_itemtype_id_3c5bccce96642ac7_fk_goods_itemtype_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_types
    ADD CONSTRAINT goods_item_ty_itemtype_id_3c5bccce96642ac7_fk_goods_itemtype_id FOREIGN KEY (itemtype_id) REFERENCES public.goods_itemtype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: goods_item_types_item_id_60b367b381990a0b_fk_goods_item_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.goods_item_types
    ADD CONSTRAINT goods_item_types_item_id_60b367b381990a0b_fk_goods_item_id FOREIGN KEY (item_id) REFERENCES public.goods_item(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_o_payment_id_1b75c3abdcea4579_fk_yandex_money_payment_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_o_payment_id_1b75c3abdcea4579_fk_yandex_money_payment_id FOREIGN KEY (payment_id) REFERENCES public.yandex_money_payment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders_order_basket_id_2cf0a8adc602a5c0_fk_basket_basket_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.orders_order
    ADD CONSTRAINT orders_order_basket_id_2cf0a8adc602a5c0_fk_basket_basket_id FOREIGN KEY (basket_id) REFERENCES public.basket_basket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yandex_money_payment_user_id_7d26368ca4d5d1fa_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cvetomaster
--

ALTER TABLE ONLY public.yandex_money_payment
    ADD CONSTRAINT yandex_money_payment_user_id_7d26368ca4d5d1fa_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

