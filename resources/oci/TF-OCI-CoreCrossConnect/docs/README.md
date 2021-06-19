# TF::OCI::CoreCrossConnect

This resource provides the Cross Connect resource in Oracle Cloud Infrastructure Core service.

Creates a new cross-connect. Oracle recommends you create each cross-connect in a
[CrossConnectGroup](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/CrossConnectGroup) so you can use link aggregation
with the connection.

After creating the `CrossConnect` object, you need to go the FastConnect location
and request to have the physical cable installed. For more information, see
[FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

For the purposes of access control, you must provide the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
compartment where you want the cross-connect to reside. If you're
not sure which compartment to use, put the cross-connect in the
same compartment with your VCN. For more information about
compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreCrossConnect",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#crossconnectgroupid" title="CrossConnectGroupId">CrossConnectGroupId</a>" : <i>String</i>,
        "<a href="#customerreferencename" title="CustomerReferenceName">CustomerReferenceName</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#farcrossconnectorcrossconnectgroupid" title="FarCrossConnectOrCrossConnectGroupId">FarCrossConnectOrCrossConnectGroupId</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#isactive" title="IsActive">IsActive</a>" : <i>Boolean</i>,
        "<a href="#locationname" title="LocationName">LocationName</a>" : <i>String</i>,
        "<a href="#nearcrossconnectorcrossconnectgroupid" title="NearCrossConnectOrCrossConnectGroupId">NearCrossConnectOrCrossConnectGroupId</a>" : <i>String</i>,
        "<a href="#portspeedshapename" title="PortSpeedShapeName">PortSpeedShapeName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreCrossConnect
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#crossconnectgroupid" title="CrossConnectGroupId">CrossConnectGroupId</a>: <i>String</i>
    <a href="#customerreferencename" title="CustomerReferenceName">CustomerReferenceName</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#farcrossconnectorcrossconnectgroupid" title="FarCrossConnectOrCrossConnectGroupId">FarCrossConnectOrCrossConnectGroupId</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#isactive" title="IsActive">IsActive</a>: <i>Boolean</i>
    <a href="#locationname" title="LocationName">LocationName</a>: <i>String</i>
    <a href="#nearcrossconnectorcrossconnectgroupid" title="NearCrossConnectOrCrossConnectGroupId">NearCrossConnectOrCrossConnectGroupId</a>: <i>String</i>
    <a href="#portspeedshapename" title="PortSpeedShapeName">PortSpeedShapeName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment to contain the cross-connect.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossConnectGroupId

The OCID of the cross-connect group to put this cross-connect in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerReferenceName

(Updatable) A reference name or identifier for the physical fiber connection that this cross-connect uses.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FarCrossConnectOrCrossConnectGroupId

If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on a different router (for the purposes of redundancy), provide the OCID of that existing cross-connect or cross-connect group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsActive

(Updatable) Set to true to activate the cross-connect. You activate it after the physical cabling is complete, and you've confirmed the cross-connect's light levels are good and your side of the interface is up. Activation indicates to Oracle that the physical connection is ready.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationName

The name of the FastConnect location where this cross-connect will be installed. To get a list of the available locations, see [ListCrossConnectLocations](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CrossConnectLocation/ListCrossConnectLocations).  Example: `CyrusOne, Chandler, AZ`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NearCrossConnectOrCrossConnectGroupId

If you already have an existing cross-connect or cross-connect group at this FastConnect location, and you want this new cross-connect to be on the same router, provide the OCID of that existing cross-connect or cross-connect group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortSpeedShapeName

The port speed for this cross-connect. To get a list of the available port speeds, see [ListCrossConnectPortSpeedShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/CrossConnectPortSpeedShape/ListCrossconnectPortSpeedShapes).  Example: `10 Gbps`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### PortName

Returns the <code>PortName</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

