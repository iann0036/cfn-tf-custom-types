# Terraform::Grafana::Organization

The organization resource allows Grafana organizations and their membership to
be created and managed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Grafana::Organization",
    "Properties" : {
        "<a href="#adminuser" title="AdminUser">AdminUser</a>" : <i>String</i>,
        "<a href="#admins" title="Admins">Admins</a>" : <i>[ String, ... ]</i>,
        "<a href="#createusers" title="CreateUsers">CreateUsers</a>" : <i>Boolean</i>,
        "<a href="#editors" title="Editors">Editors</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#viewers" title="Viewers">Viewers</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Grafana::Organization
Properties:
    <a href="#adminuser" title="AdminUser">AdminUser</a>: <i>String</i>
    <a href="#admins" title="Admins">Admins</a>: <i>
      - String</i>
    <a href="#createusers" title="CreateUsers">CreateUsers</a>: <i>Boolean</i>
    <a href="#editors" title="Editors">Editors</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#viewers" title="Viewers">Viewers</a>: <i>
      - String</i>
</pre>

## Properties

#### AdminUser

The login name of the configured
[default admin user](http://docs.grafana.org/installation/configuration/#admin-user)
for the Grafana installation. If unset, this value defaults to `admin`, the
Grafana default. Grafana adds the default admin user to all organizations
automatically upon creation, and this parameter keeps Terraform from removing
it from organizations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admins

A list of email addresses corresponding to users who
should be given `admin` access to the organization. Note: users specified
here must already exist in Grafana unless 'create_users' is set to true.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateUsers

Whether or not to create Grafana users specified
in the organization's membership if they don't already exist in Grafana. If
unspecified, this parameter defaults to `true`, creating placeholder users
with the `name`, `login`, and `email` set to the email of the user, and a
random password. Setting this option to `false` will cause an error to be
thrown for any users that do not already exist in Grafana.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Editors

A list of email addresses corresponding to users who
should be given `editor` access to the organization. Note: users specified
here must already exist in Grafana unless 'create_users' is set to true.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The display name for the Grafana organization created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Viewers

A list of email addresses corresponding to users who
should be given `viewer` access to the organization. Note: users specified
here must already exist in Grafana unless 'create_users' is set to true.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### OrgId

Returns the <code>OrgId</code> value.

