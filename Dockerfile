FROM alpine:latest as stage-preparacion
WORKDIR /app
COPY index.html .

FROM nginx:alpine
COPY --from=stage-preparacion /app/index.html /usr/share/nginx/html/index.html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
