import React from "react";
import { Phone, Mail, MapPin, Clock, Instagram, Send } from "lucide-react";
import { Card } from "./ui/card";

export function Contact() {
  const contactInfo = [
    {
      icon: Phone,
      title: "Telefon",
      details: ["+998 94 077 01 36"],
    },
    {
      icon: Mail,
      title: "Email",
      details: ["sufievabubakr509@gmail.com"],
    },
    {
      icon: MapPin,
      title: "Manzil",
      details: ["Andijon viloyati, Marhamat tumani,", "Shorqishloq 8-uy"],
    },
    {
      icon: Clock,
      title: "Ish vaqti",
      details: ["Har kuni: 06:00 - 22:00"],
    },
  ];

  return (
    <section id="contact" className="py-20 bg-slate-50 dark:bg-slate-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl mb-4 text-slate-900 dark:text-white">
            Biz Bilan Bog'laning
          </h2>
          <p className="text-xl text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">
            Savollaringiz bormi? Biz sizga yordam berishdan mamnun bo'lamiz
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          {contactInfo.map((item, index) => {
            const Icon = item.icon;
            return (
              <Card
                key={index}
                className="p-6 text-center bg-white dark:bg-slate-800 hover:shadow-lg transition-shadow"
              >
                <div className="w-14 h-14 bg-emerald-100 dark:bg-emerald-900/30 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Icon className="h-6 w-6 text-emerald-600 dark:text-emerald-400" />
                </div>
                <h3 className="text-lg mb-3 text-slate-900 dark:text-white">
                  {item.title}
                </h3>
                {item.details.map((detail, idx) => (
                  <p
                    key={idx}
                    className="text-slate-600 dark:text-slate-400 text-sm"
                  >
                    {detail}
                  </p>
                ))}
              </Card>
            );
          })}
        </div>

        {/* Map and Social Media */}
        <Card className="p-8 bg-white dark:bg-slate-800">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Map Placeholder */}
            <div className="bg-slate-200 dark:bg-slate-700 rounded-lg h-[300px] flex items-center justify-center">
              <div className="text-center">
                <MapPin className="h-12 w-12 text-slate-400 dark:text-slate-500 mx-auto mb-2" />
                <p className="text-slate-600 dark:text-slate-400">Xarita</p>
                <p className="text-sm text-slate-500 dark:text-slate-500">
                  Google Maps joylashuvi
                </p>
              </div>
            </div>

            {/* Social Media and Additional Info */}
            <div className="flex flex-col justify-center">
              <h3 className="text-2xl mb-6 text-slate-900 dark:text-white">
                Ijtimoiy Tarmoqlarda
              </h3>
              <div className="space-y-4 mb-8">
                <a
                  href="https://instagram.com/abubakirivich_sj"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-3 text-slate-700 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors"
                >
                  <div className="w-10 h-10 bg-emerald-100 dark:bg-emerald-900/30 rounded-full flex items-center justify-center">
                    <Instagram className="h-5 w-5 text-emerald-600 dark:text-emerald-400" />
                  </div>
                  <span>@abubakirivich_sj</span>
                </a>
                <a
                  href="https://t.me/+998940770136"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-3 text-slate-700 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors"
                >
                  <div className="w-10 h-10 bg-emerald-100 dark:bg-emerald-900/30 rounded-full flex items-center justify-center">
                    <Send className="h-5 w-5 text-emerald-600 dark:text-emerald-400" />
                  </div>
                  <span>+998 94 077 01 36</span>
                </a>
                <a
                  href="https://t.me/+998200077013"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-3 text-slate-700 dark:text-slate-300 hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors"
                >
                  <div className="w-10 h-10 bg-emerald-100 dark:bg-emerald-900/30 rounded-full flex items-center justify-center">
                    <Send className="h-5 w-5 text-emerald-600 dark:text-emerald-400" />
                  </div>
                  <span>+998 20 007 70 13</span>
                </a>
              </div>
              <p className="text-slate-600 dark:text-slate-400 leading-relaxed">
                Bizning ijtimoiy tarmoqlarimizda xijama va sog'lom turmush tarzi
                haqida muntazam yangiliklar, maslahatlar va maxsus takliflar bilan
                tanishing.
              </p>
            </div>
          </div>
        </Card>
      </div>
    </section>
  );
}
