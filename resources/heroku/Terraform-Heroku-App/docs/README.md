# Terraform::Heroku::App

Provides a Heroku App resource. This can be used to
create and manage applications on Heroku.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::App",
    "Properties" : {
        "<a href="#acm" title="Acm">Acm</a>" : <i>Boolean</i>,
        "<a href="#buildpacks" title="Buildpacks">Buildpacks</a>" : <i>[ String, ... ]</i>,
        "<a href="#configvars" title="ConfigVars">ConfigVars</a>" : <i>[ <a href="configvars.md">ConfigVars</a>, ... ]</i>,
        "<a href="#internalrouting" title="InternalRouting">InternalRouting</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sensitiveconfigvars" title="SensitiveConfigVars">SensitiveConfigVars</a>" : <i>[ <a href="sensitiveconfigvars.md">SensitiveConfigVars</a>, ... ]</i>,
        "<a href="#space" title="Space">Space</a>" : <i>String</i>,
        "<a href="#stack" title="Stack">Stack</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>[ <a href="organization.md">Organization</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::App
Properties:
    <a href="#acm" title="Acm">Acm</a>: <i>Boolean</i>
    <a href="#buildpacks" title="Buildpacks">Buildpacks</a>: <i>
      - String</i>
    <a href="#configvars" title="ConfigVars">ConfigVars</a>: <i>
      - <a href="configvars.md">ConfigVars</a></i>
    <a href="#internalrouting" title="InternalRouting">InternalRouting</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sensitiveconfigvars" title="SensitiveConfigVars">SensitiveConfigVars</a>: <i>
      - <a href="sensitiveconfigvars.md">SensitiveConfigVars</a></i>
    <a href="#space" title="Space">Space</a>: <i>String</i>
    <a href="#stack" title="Stack">Stack</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>
      - <a href="organization.md">Organization</a></i>
</pre>

## Properties

#### Acm

The flag representing Automated Certificate Management for the app.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Buildpacks

Buildpack names or URLs for the application.
Buildpacks configured externally won't be altered if this is not present.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigVars

_Required_: No

_Type_: List of <a href="configvars.md">ConfigVars</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalRouting

If true, the application will be routable
only internally in a private space. This option is only available for apps
that also specify `space`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the application. In Heroku, this is also the
unique ID, so it must be unique and have a minimum of 3 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region that the app should be deployed in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveConfigVars

_Required_: No

_Type_: List of <a href="sensitiveconfigvars.md">SensitiveConfigVars</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Space

The name of a private space to create the app in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stack

The application stack is what platform to run the application
in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: List of <a href="organization.md">Organization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllConfigVars

Returns the <code>AllConfigVars</code> value.

#### GitUrl

Returns the <code>GitUrl</code> value.

#### HerokuHostname

Returns the <code>HerokuHostname</code> value.

#### WebUrl

Returns the <code>WebUrl</code> value.

