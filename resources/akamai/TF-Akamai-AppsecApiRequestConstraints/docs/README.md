# TF::Akamai::AppsecApiRequestConstraints

CloudFormation equivalent of akamai_appsec_api_request_constraints

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecApiRequestConstraints",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#apiendpointid" title="ApiEndpointId">ApiEndpointId</a>" : <i>Double</i>,
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecApiRequestConstraints
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#apiendpointid" title="ApiEndpointId">ApiEndpointId</a>: <i>Double</i>
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiEndpointId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

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
