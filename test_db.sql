PGDMP                          {            test_db    15.1    15.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398    test_db    DATABASE     ~   CREATE DATABASE test_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE test_db;
                postgres    false            ?            1259    16400    persona    TABLE     ?   CREATE TABLE public.persona (
    id_persona integer NOT NULL,
    nombre character varying,
    apellido character varying,
    email character varying
);
    DROP TABLE public.persona;
       public         heap    postgres    false            ?            1259    16399    persona_id:persona_seq    SEQUENCE     ?   CREATE SEQUENCE public."persona_id:persona_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public."persona_id:persona_seq";
       public          postgres    false    215                       0    0    persona_id:persona_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public."persona_id:persona_seq" OWNED BY public.persona.id_persona;
          public          postgres    false    214            ?            1259    16422    usuarios    TABLE     ?   CREATE TABLE public.usuarios (
    id_usuario integer NOT NULL,
    username character varying,
    password character varying
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            ?            1259    16421    usuarios_id_usuario_seq    SEQUENCE     ?   CREATE SEQUENCE public.usuarios_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.usuarios_id_usuario_seq;
       public          postgres    false    217            	           0    0    usuarios_id_usuario_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.usuarios_id_usuario_seq OWNED BY public.usuarios.id_usuario;
          public          postgres    false    216            j           2604    16403    persona id_persona    DEFAULT     z   ALTER TABLE ONLY public.persona ALTER COLUMN id_persona SET DEFAULT nextval('public."persona_id:persona_seq"'::regclass);
 A   ALTER TABLE public.persona ALTER COLUMN id_persona DROP DEFAULT;
       public          postgres    false    214    215    215            k           2604    16425    usuarios id_usuario    DEFAULT     z   ALTER TABLE ONLY public.usuarios ALTER COLUMN id_usuario SET DEFAULT nextval('public.usuarios_id_usuario_seq'::regclass);
 B   ALTER TABLE public.usuarios ALTER COLUMN id_usuario DROP DEFAULT;
       public          postgres    false    217    216    217            ?          0    16400    persona 
   TABLE DATA           F   COPY public.persona (id_persona, nombre, apellido, email) FROM stdin;
    public          postgres    false    215   ?                 0    16422    usuarios 
   TABLE DATA           B   COPY public.usuarios (id_usuario, username, password) FROM stdin;
    public          postgres    false    217   c       
           0    0    persona_id:persona_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."persona_id:persona_seq"', 14, true);
          public          postgres    false    214                       0    0    usuarios_id_usuario_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.usuarios_id_usuario_seq', 5, true);
          public          postgres    false    216            m           2606    16407    persona persona_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.persona
    ADD CONSTRAINT persona_pkey PRIMARY KEY (id_persona);
 >   ALTER TABLE ONLY public.persona DROP CONSTRAINT persona_pkey;
       public            postgres    false    215            o           2606    16429    usuarios usuarios_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public            postgres    false    217            ?   ?   x?M?=?0E??Sl-????ଓ??%5?6??M*?,?^8???!?6?????{Ҏ?6?:?1J?B?%?5*???`=~t?_???Ð?[d??Ú?J?p?3?Kpz??U???q^??X?'?ѐy??ẙL?l??o2yќ????R???VL         O   x?3?t?()J???t,N142?2?L.MJ???L*J?2?LK??,????L?*MN,?2??L.?/?L?H?I???????? ??     