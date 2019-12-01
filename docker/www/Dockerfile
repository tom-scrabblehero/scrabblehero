FROM node:10-alpine3.9

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN npm install

CMD npm run serve
