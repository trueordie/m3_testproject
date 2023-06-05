from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


class UsersEditWindow(BaseEditWindow):

    def _init_components(self) -> None:
        super(UsersEditWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label='Имя пользователя',
            name='username',
            allow_blank=False,
            anchor='100%',
        )
        self.field__name = ext.ExtStringField(
            label='Имя',
            name='first_name',
            allow_blank=False,
            anchor='100%',
        )
        self.field__surname = ext.ExtStringField(
            label='Фамилия',
            name='last_name',
            allow_blank=False,
            anchor='100%',
        )
        self.field__email = ext.ExtStringField(
            label='E-Mail',
            name='email',
            allow_blank=False,
            anchor='100%',
        )
        self.field__password = ext.ExtStringField(
            label='Пароль',
            name='password',
            allow_blank=False,
            anchor='100%',
        )
        self.field__su_status = ext.ExtCheckBox(
            label='Статус суперпользователя',
            name='is_superuser',
            allow_blank=True,
            anchor='100%',
        )
        self.field_staff_status = ext.ExtCheckBox(
            label='Статус обычного пользователя',
            name='is_staff',
            allow_blank=True,
            anchor='100%',
        )
        self.field_active_status = ext.ExtCheckBox(
            label='Активен',
            name='is_active',
            allow_blank=True,
            anchor='100%',
        )
        self.field_date_joined = ext.ExtDateField(
            label='Дата добавления',
            name='date_joined',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y',
        )

    def _do_layout(self) -> None:
        super(UsersEditWindow, self)._do_layout()
        self.form.items.extend([
            self.field__username,
            self.field__name,
            self.field__surname,
            self.field__email,
            self.field__password,
            self.field__su_status,
            self.field_staff_status,
            self.field_active_status,
            self.field_date_joined,
        ])

    def set_params(self, params) -> None:
        super(UsersEditWindow, self).set_params(params)
        self.height = 'auto'
