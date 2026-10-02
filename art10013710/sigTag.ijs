NB.* sigTag.ijs: tag a bitmap of a hand-written personal signature with info.

load 'images'

NB. This was swiped from groupPix.ijs:
getChars=: 3 : 0
NB.* getChars: get fixed-size characters from mat picture.
   chrs=. read_image_ima3_ '\amisc\txt\chars16x16_32x22_3.jpg'
NB. '\amisc\txt\chars16x16_32x22.jpg'
   chrsz=. 16%~2{.$chrs
   ch16=. ((2{.$chrs)$&.>chrsz{.&.>1)<;.1 chrs
   ch16=. 255*&.>128<&.>ch16       NB. make black and white
   ix=. 3 4 5                      NB. Uppercase char rows.
   ul=. (whul=. a. i. '_'){,ch16   NB. Save underline because will get trimmed.
   upcs=. 6}.&.>_8}.&.>_8}."2&.>3}."2&.>ix{ch16
   ul=. <5}._7}._7}."(2)2}."(2) >ul     NB. Trim "_" one less than uppercase
   ch16=. (upcs) ix}ch16
   ch16=. (ul) (<16 16#:whul)}ch16 NB. Put back underline trimmed out.
)

NB.* maxctr: make all bitmaps max size and centered.
maxctr=: 4 : '255-(0{x.)|._1 ] (1{.x.)|."2 ] (-x.){.255-y.'

tagSigWithMsg=: 3 : 0
NB. tagSigWithMsg: insert message into bitmap of signature->new bitmap.
   'msg sigfl'=. y.
   mysig=. read_image sigfl
   ch16=. getChars ''
   msgch=. (a. i. msg){,ch16
   maxsz=. >./$&>msgch
   xclnp=. msg e. '0123456789.,;'':_`"' NB. Don't center numerals and punc'n.
   msgc2=. (<maxsz) maxctr&.>msgch      NB. letters all same size and centered
   msgch=. xclnp}msgc2,:msgch
   bitmsg=. >,&.>/(1 0 2&|:)&.>msgch    NB. correct orientation
   bitmsg=. 3#"2 bitmsg                 NB. Make letters taller=more legible
NB. XOR bits of insertion and signature; position insertion in lower-right.
   newsig=. 255<.#.((8$2)#:mysig)~:(_8,~-$mysig){.-.(8$2)#:1 0 2|:bitmsg
NB.EG newsig=. tagSigWithMsg 'name and date';'my thin blue signature.bmp'
)

createNewSigBMP=: 3 : 0
NB.* createNewSigBMP: create new bitmap file: signature with embedded message.
   'msg sigfl newfl'=. y.
   newsig=. tagSigWithMsg msg;sigfl
   newsig write_image newfl
NB.EG flsz=. createNewSigBMP 'DHM 20050608 14:34';'mysig.bmp';'sig5680234.bmp'
)
