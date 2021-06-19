# TF::Aviatrix::FirewallPolicy

The **aviatrix_firewall_policy** resource manages a single Stateful Firewall policy resource.

~> **NOTE on Firewall and Firewall Policy resources:** Terraform currently provides both a standalone Firewall Policy resource and a Firewall resource with policies defined in-line. At this time, you cannot use a Firewall resource with in-line rules in conjunction with any Firewall Policy resources. Doing so will cause a conflict of policy settings and will overwrite policies. In order to use this resource, please set `manage_firewall_policies` in the **aviatrix_firewall** resource to false.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::FirewallPolicy",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dstip" title="DstIp">DstIp</a>" : <i>String</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#logenabled" title="LogEnabled">LogEnabled</a>" : <i>Boolean</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#srcip" title="SrcIp">SrcIp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::FirewallPolicy
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dstip" title="DstIp">DstIp</a>: <i>String</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#logenabled" title="LogEnabled">LogEnabled</a>: <i>Boolean</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#srcip" title="SrcIp">SrcIp</a>: <i>String</i>
</pre>

## Properties

#### Action

Valid values: "allow", "deny" and "force-drop" (in stateful firewall rule to allow immediate packet dropping on established sessions).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the policy. Example: "This is policy no.1".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstIp

CIDRs separated by comma or tag names such "HR" or "marketing" etc. Example: "10.30.0.0/16,10.45.0.0/20". The **aviatrix_firewall_tag** resource should be created prior to using the tag name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName

Gateway name to attach firewall policy to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogEnabled

Valid values: true, false. Default value: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

A single port or a range of port numbers. Example: "25", "25:1024".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

: "all", "tcp", "udp", "icmp", "sctp", "rdp", "dccp".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcIp

CIDRs separated by comma or tag names such "HR" or "marketing" etc. Example: "10.30.0.0/16,10.45.0.0/20". The **aviatrix_firewall_tag** resource should be created prior to using the tag name.

_Required_: Yes

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

