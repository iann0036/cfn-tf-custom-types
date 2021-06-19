# TF::Heroku::AppConfigAssociation

Provides a Heroku App Config Association resource, making it possible to set/update/remove heroku app config vars independently from
the `heroku_app` resource. An example usage scenario could be:

* User has separate git repositories for various micro-services. Multiple micro-services use Kafka.
* User has a separate repository for kafka terraform files with blue/green support.
* User builds out new clusters.
* Prior to this resource's introduction, user would need one `terraform apply` to update state and X number of `terraform apply`
for each micro-service to pick up the new kafka clusters. However with this resource, user can do one `terraform apply`
and let Heroku handle the rolling restarts to pick up the new config vars.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Heroku::AppConfigAssociation",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>" : <i>[ <a href="sensitivevarsdefinition.md">SensitiveVarsDefinition</a>, ... ]</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="varsdefinition.md">VarsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Heroku::AppConfigAssociation
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#sensitivevars" title="SensitiveVars">SensitiveVars</a>: <i>
      - <a href="sensitivevarsdefinition.md">SensitiveVarsDefinition</a></i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="varsdefinition.md">VarsDefinition</a></i>
</pre>

## Properties

#### AppId

A Heroku app's `UUID`. Can also be the name of the Heroku app but `UUID` is preferred as it is idempotent.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveVars

This is the same as `vars`. The main difference between the two
attributes is `sensitive_vars` outputs are redacted on-screen and replaced by a <sensitive> placeholder, following a terraform
plan or apply. It is recommended to put private keys, passwords, etc in this argument.

_Required_: No

_Type_: List of <a href="sensitivevarsdefinition.md">SensitiveVarsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

Map of config vars that can be output in plaintext.

_Required_: No

_Type_: List of <a href="varsdefinition.md">VarsDefinition</a>

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

