# Terraform::Heroku::App

CloudFormation equivalent of heroku_app

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::App",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#acm" title="Acm">Acm</a>" : <i>Boolean</i>,
        "<a href="#allconfigvars" title="AllConfigVars">AllConfigVars</a>" : <i>[ &lt;a href=&#34;allconfigvars.md&#34;&gt;AllConfigVars&lt;/a&gt;, ... ]</i>,
        "<a href="#buildpacks" title="Buildpacks">Buildpacks</a>" : <i>[ String, ... ]</i>,
        "<a href="#configvars" title="ConfigVars">ConfigVars</a>" : <i>[ &lt;a href=&#34;configvars.md&#34;&gt;ConfigVars&lt;/a&gt;, ... ]</i>,
        "<a href="#giturl" title="GitUrl">GitUrl</a>" : <i>String</i>,
        "<a href="#herokuhostname" title="HerokuHostname">HerokuHostname</a>" : <i>String</i>,
        "<a href="#internalrouting" title="InternalRouting">InternalRouting</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sensitiveconfigvars" title="SensitiveConfigVars">SensitiveConfigVars</a>" : <i>[ &lt;a href=&#34;sensitiveconfigvars.md&#34;&gt;SensitiveConfigVars&lt;/a&gt;, ... ]</i>,
        "<a href="#space" title="Space">Space</a>" : <i>String</i>,
        "<a href="#stack" title="Stack">Stack</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#weburl" title="WebUrl">WebUrl</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>[ &lt;a href=&#34;organization.md&#34;&gt;Organization&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::App
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#acm" title="Acm">Acm</a>: <i>Boolean</i>
    <a href="#allconfigvars" title="AllConfigVars">AllConfigVars</a>: <i>
      - &lt;a href=&#34;allconfigvars.md&#34;&gt;AllConfigVars&lt;/a&gt;</i>
    <a href="#buildpacks" title="Buildpacks">Buildpacks</a>: <i>
      - String</i>
    <a href="#configvars" title="ConfigVars">ConfigVars</a>: <i>
      - &lt;a href=&#34;configvars.md&#34;&gt;ConfigVars&lt;/a&gt;</i>
    <a href="#giturl" title="GitUrl">GitUrl</a>: <i>String</i>
    <a href="#herokuhostname" title="HerokuHostname">HerokuHostname</a>: <i>String</i>
    <a href="#internalrouting" title="InternalRouting">InternalRouting</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sensitiveconfigvars" title="SensitiveConfigVars">SensitiveConfigVars</a>: <i>
      - &lt;a href=&#34;sensitiveconfigvars.md&#34;&gt;SensitiveConfigVars&lt;/a&gt;</i>
    <a href="#space" title="Space">Space</a>: <i>String</i>
    <a href="#stack" title="Stack">Stack</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#weburl" title="WebUrl">WebUrl</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>
      - &lt;a href=&#34;organization.md&#34;&gt;Organization&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acm

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllConfigVars

_Required_: No

_Type_: List of &lt;a href=&#34;allconfigvars.md&#34;&gt;AllConfigVars&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Buildpacks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigVars

_Required_: No

_Type_: List of &lt;a href=&#34;configvars.md&#34;&gt;ConfigVars&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HerokuHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalRouting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveConfigVars

_Required_: No

_Type_: List of &lt;a href=&#34;sensitiveconfigvars.md&#34;&gt;SensitiveConfigVars&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Space

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: List of &lt;a href=&#34;organization.md&#34;&gt;Organization&lt;/a&gt;

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

Returns the &lt;code&gt;AllConfigVars&lt;/code&gt; value.

#### GitUrl

Returns the &lt;code&gt;GitUrl&lt;/code&gt; value.

#### HerokuHostname

Returns the &lt;code&gt;HerokuHostname&lt;/code&gt; value.

#### WebUrl

Returns the &lt;code&gt;WebUrl&lt;/code&gt; value.

