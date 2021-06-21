# TF::Akamai::AppsecSecurityPolicy

Use the `akamai_appsec_security_policy` resource to create a new security policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecSecurityPolicy",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#defaultsettings" title="DefaultSettings">DefaultSettings</a>" : <i>Boolean</i>,
        "<a href="#securitypolicyname" title="SecurityPolicyName">SecurityPolicyName</a>" : <i>String</i>,
        "<a href="#securitypolicyprefix" title="SecurityPolicyPrefix">SecurityPolicyPrefix</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecSecurityPolicy
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#defaultsettings" title="DefaultSettings">DefaultSettings</a>: <i>Boolean</i>
    <a href="#securitypolicyname" title="SecurityPolicyName">SecurityPolicyName</a>: <i>String</i>
    <a href="#securitypolicyprefix" title="SecurityPolicyPrefix">SecurityPolicyPrefix</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### ConfigId

The configuration ID to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSettings

Whether the new policy should use the default settings. If not supplied, defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyName

The name of the new security policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version number of the configuration to use.

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

#### SecurityPolicyId

Returns the <code>SecurityPolicyId</code> value.
