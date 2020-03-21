# Terraform::OCI::CoreSecurityList

This resource provides the Security List resource in Oracle Cloud Infrastructure Core service.

Creates a new security list for the specified VCN. For more information
about security lists, see [Security Lists](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securitylists.htm).
For information on the number of rules you can have in a security list, see
[Service Limits](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want the security
list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets,
or other Networking Service components. If you're not sure which compartment to use, put the security
list in the same compartment as the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the security list, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information on configuring a VCN's default security list, see [Managing Default VCN Resources](/docs/providers/oci/guides/managing_default_resources.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreSecurityList",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#vcnid" title="VcnId">VcnId</a>" : <i>String</i>,
        "<a href="#egresssecurityrules" title="EgressSecurityRules">EgressSecurityRules</a>" : <i>[ <a href="egresssecurityrules.md">EgressSecurityRules</a>, ... ]</i>,
        "<a href="#ingresssecurityrules" title="IngressSecurityRules">IngressSecurityRules</a>" : <i>[ <a href="ingresssecurityrules.md">IngressSecurityRules</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>" : <i>[ <a href="icmpoptions.md">IcmpOptions</a>, ... ]</i>,
        "<a href="#tcpoptions" title="TcpOptions">TcpOptions</a>" : <i>[ <a href="tcpoptions.md">TcpOptions</a>, ... ]</i>,
        "<a href="#udpoptions" title="UdpOptions">UdpOptions</a>" : <i>[ <a href="udpoptions.md">UdpOptions</a>, ... ]</i>,
        "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>[ <a href="sourceportrange.md">SourcePortRange</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreSecurityList
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#vcnid" title="VcnId">VcnId</a>: <i>String</i>
    <a href="#egresssecurityrules" title="EgressSecurityRules">EgressSecurityRules</a>: <i>
      - <a href="egresssecurityrules.md">EgressSecurityRules</a></i>
    <a href="#ingresssecurityrules" title="IngressSecurityRules">IngressSecurityRules</a>: <i>
      - <a href="ingresssecurityrules.md">IngressSecurityRules</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>: <i>
      - <a href="icmpoptions.md">IcmpOptions</a></i>
    <a href="#tcpoptions" title="TcpOptions">TcpOptions</a>: <i>
      - <a href="tcpoptions.md">TcpOptions</a></i>
    <a href="#udpoptions" title="UdpOptions">UdpOptions</a>: <i>
      - <a href="udpoptions.md">UdpOptions</a></i>
    <a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>
      - <a href="sourceportrange.md">SourcePortRange</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment to contain the security list.

_Required_: Yes

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

#### VcnId

The OCID of the VCN the security list belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressSecurityRules

_Required_: No

_Type_: List of <a href="egresssecurityrules.md">EgressSecurityRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressSecurityRules

_Required_: No

_Type_: List of <a href="ingresssecurityrules.md">IngressSecurityRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpOptions

_Required_: No

_Type_: List of <a href="icmpoptions.md">IcmpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpOptions

_Required_: No

_Type_: List of <a href="tcpoptions.md">TcpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpOptions

_Required_: No

_Type_: List of <a href="udpoptions.md">UdpOptions</a>

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

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

