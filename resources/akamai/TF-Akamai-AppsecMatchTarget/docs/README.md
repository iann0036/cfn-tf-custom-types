# TF::Akamai::AppsecMatchTarget

The `akamai_appsec_match_target` resource allows you to create or modify a match target associated with a given security configuration version.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecMatchTarget",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#matchtarget" title="MatchTarget">MatchTarget</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecMatchTarget
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#matchtarget" title="MatchTarget">MatchTarget</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### ConfigId

The ID of the security configuration to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchTarget

The name of a JSON file containing one or more match target definitions ([format](https://developer.akamai.com/api/cloud_security/application_security/v1.html#postmatchtargets)).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version number of the security configuration to use.

_Required_: Yes

_Type_: Double

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

#### MatchTargetId

Returns the <code>MatchTargetId</code> value.
