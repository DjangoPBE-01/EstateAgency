from rest_framework_simplejwt.authentication import JWTAuthentication


class SwaggerFriendlyJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        header = super().get_header(request)
        if header:
            return header

        raw_header = request.META.get("HTTP_AUTHORIZATION")
        if not raw_header:
            return None

        raw_header = raw_header.strip()
        if raw_header.lower().startswith("bearer "):
            return raw_header.encode()

        return f"Bearer {raw_header}".encode()