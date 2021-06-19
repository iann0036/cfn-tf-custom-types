# TF::FortiOS::FmgFirewallSecurityPolicypackage

This resource supports Create/Read/Update/Delete firewall security policypackage on FortiManager which could be installed to the FortiGate later

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FmgFirewallSecurityPolicypackage",
    "Properties" : {
        "<a href="#adom" title="Adom">Adom</a>" : <i>String</i>,
        "<a href="#inspectionmode" title="InspectionMode">InspectionMode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FmgFirewallSecurityPolicypackage
Properties:
    <a href="#adom" title="Adom">Adom</a>: <i>String</i>
    <a href="#inspectionmode" title="InspectionMode">InspectionMode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>String</i>
</pre>

## Properties

#### Adom

Source ADOM name. default is 'root'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectionMode

Inspection Mode. Enum:[flow, proxy]. default is 'flow'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Security policy package name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

The installation target.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

Vdom of managed device. default is 'root'.

_Required_: No

_Type_: String

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

