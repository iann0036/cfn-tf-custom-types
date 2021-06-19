# TF::Aviatrix::SpokeTransitAttachment

The **aviatrix_spoke_transit_attachment** resource allows the creation and management of Aviatrix Spoke-to-Transit gateway attachments.

~> **NOTE:** Terraform currently provides both a standalone spoke-to-transit attachment resource and a spoke gateway with `transit_gw` attachment(s) defined in-line. At this time, you cannot use a spoke gateway resource with transit attachments defined in conjunction with the spoke-to-transit attachment resources. Doing so will cause a conflict of settings. In order to use this resource, please set `manage_transit_gateway_attachment` in the **aviatrix_spoke_gateway** to false.

~> **NOTE:** This resource should only be used to manage the primary gateway attachments. The HA gateway attachments will be handled automatically by the backend.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SpokeTransitAttachment",
    "Properties" : {
        "<a href="#routetables" title="RouteTables">RouteTables</a>" : <i>[ String, ... ]</i>,
        "<a href="#spokegwname" title="SpokeGwName">SpokeGwName</a>" : <i>String</i>,
        "<a href="#transitgwname" title="TransitGwName">TransitGwName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SpokeTransitAttachment
Properties:
    <a href="#routetables" title="RouteTables">RouteTables</a>: <i>
      - String</i>
    <a href="#spokegwname" title="SpokeGwName">SpokeGwName</a>: <i>String</i>
    <a href="#transitgwname" title="TransitGwName">TransitGwName</a>: <i>String</i>
</pre>

## Properties

#### RouteTables

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpokeGwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGwName

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

