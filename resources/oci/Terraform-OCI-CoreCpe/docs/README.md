# Terraform::OCI::CoreCpe

This resource provides the Cpe resource in Oracle Cloud Infrastructure Core service.

Creates a new virtual customer-premises equipment (CPE) object in the specified compartment. For
more information, see [IPSec VPNs](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want
the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec
connection or other Networking Service components. If you're not sure which compartment to
use, put the CPE in the same compartment as the DRG. For more information about
compartments and access control, see [Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
For information about OCIDs, see [Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You must provide the public IP address of your on-premises router. See
[Configuring Your On-Premises Router for an IPSec VPN](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/configuringCPE.htm).

You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to
be unique, and you can change it. Avoid entering confidential information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreCpe",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#cpedeviceshapeid" title="CpeDeviceShapeId">CpeDeviceShapeId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreCpe
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#cpedeviceshapeid" title="CpeDeviceShapeId">CpeDeviceShapeId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment to contain the CPE.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpeDeviceShapeId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the CPE device type. You can provide a value if you want to later generate CPE device configuration content for IPSec connections that use this CPE. You can also call [UpdateCpe](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Cpe/UpdateCpe) later to provide a value. For a list of possible values, see [ListCpeDeviceShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CpeDeviceShapeSummary/ListCpeDeviceShapes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The public IP address of the on-premises router.  Example: `143.19.23.16`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

