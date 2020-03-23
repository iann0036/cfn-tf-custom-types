# Terraform::AWS::Ec2TrafficMirrorFilterRule

Provides an Traffic mirror filter rule.  
Read [limits and considerations](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-considerations.html) for traffic mirroring

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Ec2TrafficMirrorFilterRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
        "<a href="#ruleaction" title="RuleAction">RuleAction</a>" : <i>String</i>,
        "<a href="#rulenumber" title="RuleNumber">RuleNumber</a>" : <i>Double</i>,
        "<a href="#sourcecidrblock" title="SourceCidrBlock">SourceCidrBlock</a>" : <i>String</i>,
        "<a href="#trafficdirection" title="TrafficDirection">TrafficDirection</a>" : <i>String</i>,
        "<a href="#trafficmirrorfilterid" title="TrafficMirrorFilterId">TrafficMirrorFilterId</a>" : <i>String</i>,
        "<a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>" : <i>[ <a href="destinationportrange.md">DestinationPortRange</a>, ... ]</i>,
        "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>[ <a href="sourceportrange.md">SourcePortRange</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Ec2TrafficMirrorFilterRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationcidrblock" title="DestinationCidrBlock">DestinationCidrBlock</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
    <a href="#ruleaction" title="RuleAction">RuleAction</a>: <i>String</i>
    <a href="#rulenumber" title="RuleNumber">RuleNumber</a>: <i>Double</i>
    <a href="#sourcecidrblock" title="SourceCidrBlock">SourceCidrBlock</a>: <i>String</i>
    <a href="#trafficdirection" title="TrafficDirection">TrafficDirection</a>: <i>String</i>
    <a href="#trafficmirrorfilterid" title="TrafficMirrorFilterId">TrafficMirrorFilterId</a>: <i>String</i>
    <a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>: <i>
      - <a href="destinationportrange.md">DestinationPortRange</a></i>
    <a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>
      - <a href="sourceportrange.md">SourcePortRange</a></i>
</pre>

## Properties

#### Description

A description of the traffic mirror filter rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationCidrBlock

The destination CIDR block to assign to the Traffic Mirror rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol number, for example 17 (UDP), to assign to the Traffic Mirror rule. For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleAction

The action to take (accept | reject) on the filtered traffic. Valid values are `accept` and `reject`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleNumber

The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCidrBlock

The source CIDR block to assign to the Traffic Mirror rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficDirection

The direction of traffic to be captured. Valid values are `ingress` and `egress`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficMirrorFilterId

ID of the traffic mirror filter to which this rule should be added.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortRange

_Required_: No

_Type_: List of <a href="destinationportrange.md">DestinationPortRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRange

_Required_: No

_Type_: List of <a href="sourceportrange.md">SourcePortRange</a>

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

