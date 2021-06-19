# TF::Akamai::AppsecConfigurationVersionClone

The `akamai_appsec_configuration_version_clone` resource allows you to create a new version of a security configuration by cloning an existing version.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecConfigurationVersionClone",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#createfromversion" title="CreateFromVersion">CreateFromVersion</a>" : <i>Double</i>,
        "<a href="#ruleupdate" title="RuleUpdate">RuleUpdate</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecConfigurationVersionClone
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#createfromversion" title="CreateFromVersion">CreateFromVersion</a>: <i>Double</i>
    <a href="#ruleupdate" title="RuleUpdate">RuleUpdate</a>: <i>Boolean</i>
</pre>

## Properties

#### ConfigId

The ID of the security configuration to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateFromVersion

The version number of the security configuration to clone.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleUpdate

A boolean indicating whether to update the rules of the new version. If not supplied, False is assumed.

_Required_: No

_Type_: Boolean

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

#### Version

Returns the <code>Version</code> value.

