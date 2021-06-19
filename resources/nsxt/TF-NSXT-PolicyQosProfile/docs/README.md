# TF::NSXT::PolicyQosProfile

This resource provides a method for the management of Qos profiles.

This resource is applicable to NSX Global Manager, NSX Policy Manager and VMC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyQosProfile",
    "Properties" : {
        "<a href="#classofservice" title="ClassOfService">ClassOfService</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dscppriority" title="DscpPriority">DscpPriority</a>" : <i>Double</i>,
        "<a href="#dscptrusted" title="DscpTrusted">DscpTrusted</a>" : <i>Boolean</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#egressrateshaper" title="EgressRateShaper">EgressRateShaper</a>" : <i>[ <a href="egressrateshaperdefinition.md">EgressRateShaperDefinition</a>, ... ]</i>,
        "<a href="#ingressbroadcastrateshaper" title="IngressBroadcastRateShaper">IngressBroadcastRateShaper</a>" : <i>[ <a href="ingressbroadcastrateshaperdefinition.md">IngressBroadcastRateShaperDefinition</a>, ... ]</i>,
        "<a href="#ingressrateshaper" title="IngressRateShaper">IngressRateShaper</a>" : <i>[ <a href="ingressrateshaperdefinition.md">IngressRateShaperDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyQosProfile
Properties:
    <a href="#classofservice" title="ClassOfService">ClassOfService</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dscppriority" title="DscpPriority">DscpPriority</a>: <i>Double</i>
    <a href="#dscptrusted" title="DscpTrusted">DscpTrusted</a>: <i>Boolean</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#egressrateshaper" title="EgressRateShaper">EgressRateShaper</a>: <i>
      - <a href="egressrateshaperdefinition.md">EgressRateShaperDefinition</a></i>
    <a href="#ingressbroadcastrateshaper" title="IngressBroadcastRateShaper">IngressBroadcastRateShaper</a>: <i>
      - <a href="ingressbroadcastrateshaperdefinition.md">IngressBroadcastRateShaperDefinition</a></i>
    <a href="#ingressrateshaper" title="IngressRateShaper">IngressRateShaper</a>: <i>
      - <a href="ingressrateshaperdefinition.md">IngressRateShaperDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### ClassOfService

Class of service.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

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

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressRateShaper

_Required_: No

_Type_: List of <a href="egressrateshaperdefinition.md">EgressRateShaperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressBroadcastRateShaper

_Required_: No

_Type_: List of <a href="ingressbroadcastrateshaperdefinition.md">IngressBroadcastRateShaperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressRateShaper

_Required_: No

_Type_: List of <a href="ingressrateshaperdefinition.md">IngressRateShaperDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

