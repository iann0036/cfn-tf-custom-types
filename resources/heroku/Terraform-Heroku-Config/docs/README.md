# Terraform::Heroku::Config

Provides a Heroku Config resource, making it possible to define variables 
to be used throughout your Heroku terraform configurations. Combined with `heroku_app_config_association`,
these two resources enable users to decouple setting config var(s) from the `heroku_app` resource.

~> **NOTE:** Unlike most Terraform resources, this resource **DOES NOT** by itself create, update or delete anything in Heroku. 
A [`heroku_app_config_association`](app_config_association.html), `heroku_app.config_vars`, or `heroku_app.sensitive_config_vars` is required to actually set these values on Heroku apps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Config",
    "Properties" : {
        "<a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>" : <i>[ <a href="sensitivevars.md">SensitiveVars</a>, ... ]</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="vars.md">Vars</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Config
Properties:
    <a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>: <i>
      - <a href="sensitivevars.md">SensitiveVars</a></i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="vars.md">Vars</a></i>
</pre>

## Properties

#### SensitiveVars

This is the same as `vars`. The main difference between the two
attributes is `sensitive_vars` outputs are redacted on-screen and replaced by a <sensitive> placeholder, following a terraform
`plan` or `apply`. It is recommended to put private keys, passwords, etc in this argument.

_Required_: No

_Type_: List of <a href="sensitivevars.md">SensitiveVars</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

Map of vars that are can be outputted in plaintext.

_Required_: No

_Type_: List of <a href="vars.md">Vars</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

