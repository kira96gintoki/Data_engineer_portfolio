PGDMP      (                 }            spbase    17.2 (Debian 17.2-1.pgdg120+1)    17.1 	    #           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            $           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            %           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            &           1262    16388    spbase    DATABASE     q   CREATE DATABASE spbase WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE spbase;
                     postgres    false                        2615    24577    spinfo    SCHEMA        CREATE SCHEMA spinfo;
    DROP SCHEMA spinfo;
                     postgres    false            �            1259    24586     measure    TABLE       CREATE TABLE spinfo." measure" (
    device character varying,
    "co " double precision,
    humidity double precision,
    light boolean,
    lpg double precision,
    motion boolean,
    "smoke " double precision,
    temp character varying,
    ts integer
);
    DROP TABLE spinfo." measure";
       spinfo         heap r       postgres    false    6            �            1259    24581    sensor metadata    TABLE     ~   CREATE TABLE spinfo."sensor metadata" (
    "ID" integer,
    " location" character varying,
    " type" character varying
);
 %   DROP TABLE spinfo."sensor metadata";
       spinfo         heap r       postgres    false    6                       0    24586     measure 
   TABLE DATA           e   COPY spinfo." measure" (device, "co ", humidity, light, lpg, motion, "smoke ", temp, ts) FROM stdin;
    spinfo               postgres    false    219   �                 0    24581    sensor metadata 
   TABLE DATA           G   COPY spinfo."sensor metadata" ("ID", " location", " type") FROM stdin;
    spinfo               postgres    false    218   �              x������ � �            x������ � �     