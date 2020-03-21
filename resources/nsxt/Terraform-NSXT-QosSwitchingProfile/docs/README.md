# Terraform::NSXT::QosSwitchingProfile

Provides a resource to configure Qos switching profile on NSX-T manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::QosSwitchingProfile",
    "Properties" : {
        "<a href="#classofservice" title="ClassOfService">ClassOfService</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dscppriority" title="DscpPriority">DscpPriority</a>" : <i>Double</i>,
        "<a href="#dscptrusted" title="DscpTrusted">DscpTrusted</a>" : <i>Boolean</i>,
        "<a href="#egressrateshaper" title="EgressRateShaper">EgressRateShaper</a>" : <i>[ <a href="egressrateshaper.md">EgressRateShaper</a>, ... ]</i>,
        "<a href="#ingressbroadcastrateshaper" title="IngressBroadcastRateShaper">IngressBroadcastRateShaper</a>" : <i>[ <a href="ingressbroadcastrateshaper.md">IngressBroadcastRateShaper</a>, ... ]</i>,
        "<a href="#ingressrateshaper" title="IngressRateShaper">IngressRateShaper</a>" : <i>[ <a href="ingressrateshaper.md">IngressRateShaper</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::QosSwitchingProfile
Properties:
    <a href="#classofservice" title="ClassOfService">ClassOfService</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dscppriority" title="DscpPriority">DscpPriority</a>: <i>Double</i>
    <a href="#dscptrusted" title="DscpTrusted">DscpTrusted</a>: <i>Boolean</i>
    <a href="#egressrateshaper" title="EgressRateShaper">EgressRateShaper</a>: <i>
      - <a href="egressrateshaper.md">EgressRateShaper</a></i>
    <a href="#ingressbroadcastrateshaper" title="IngressBroadcastRateShaper">IngressBroadcastRateShaper</a>: <i>
      - <a href="ingressbroadcastrateshaper.md">IngressBroadcastRateShaper</a></i>
    <a href="#ingressrateshaper" title="IngressRateShaper">IngressRateShaper</a>: <i>
      - <a href="ingressrateshaper.md">IngressRateShaper</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### ClassOfService

Class of service.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpPriority

DSCP Priority (0-63).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpTrusted

Trust mode for DSCP (False by default).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressRateShaper

_Required_: No

_Type_: List of <a href="egressrateshaper.md">EgressRateShaper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressBroadcastRateShaper

_Required_: No

_Type_: List of <a href="ingressbroadcastrateshaper.md">IngressBroadcastRateShaper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressRateShaper

_Required_: No

_Type_: List of <a href="ingressrateshaper.md">IngressRateShaper</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Revision

Returns the <code>Revision</code> value.

