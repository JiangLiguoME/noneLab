/*
 * dataConv.h
 *
 *  Created on: 2018年4月19日
 *      Author: liguo
 */

#ifndef DATACONV_H_
#define DATACONV_H_
#define dataFrameMaxLength 100
#include "stdio.h"
#include "string.h"

void joinDataBody(char *dataBody,char *dataId,uint32_t *data);
void creatDataFrame(char *dataFrame,char *dataBody);

#endif /* DATACONV_H_ */
