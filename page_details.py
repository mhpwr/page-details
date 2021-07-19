def page_details(request, slug):
    site = Site.objects.get_current()
    page = get_object_or_404(
        Page.objects.prefetch_related('sections'),
        sites__in=[site, ],
        slug=slug,
    )
    utm_source = request.GET.get('utm_source')
    template = 'pages/page_details_%s.html' % page.template
    if utm_source == 'mobileapp':
        template = 'pages/page_details_mobileapp.html'
    content_type = ContentType.objects.get_for_model(page)
    photos = Photo.objects.filter(
        content_type=content_type,
        object_id=page.pk,
    ).exists()
    return render(request, template, {
        'page': page,
        'sections': page.sections.all(),
        'photos': photos,
    })
