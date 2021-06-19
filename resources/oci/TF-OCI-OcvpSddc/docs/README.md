# TF::OCI::OcvpSddc

This resource provides the Sddc resource in Oracle Cloud Infrastructure Oracle Cloud VMware Solution service.

Creates an Oracle Cloud VMware Solution software-defined data center (SDDC).

Use the [WorkRequest](https://docs.cloud.oracle.com/iaas/api/#/en/vmware/20200501/WorkRequest/) operations to track the
creation of the SDDC.

**Important:** You must configure the SDDC's networking resources with the security rules detailed in [Security Rules for Oracle Cloud VMware Solution SDDCs](https://docs.cloud.oracle.com/iaas/Content/VMware/Reference/ocvssecurityrules.htm). Otherwise, provisioning the SDDC will fail. The rules are based on the requirements set by VMware.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::OcvpSddc",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#computeavailabilitydomain" title="ComputeAvailabilityDomain">ComputeAvailabilityDomain</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#esxihostscount" title="EsxiHostsCount">EsxiHostsCount</a>" : <i>Double</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#hcxaction" title="HcxAction">HcxAction</a>" : <i>String</i>,
        "<a href="#hcxvlanid" title="HcxVlanId">HcxVlanId</a>" : <i>String</i>,
        "<a href="#initialsku" title="InitialSku">InitialSku</a>" : <i>String</i>,
        "<a href="#instancedisplaynameprefix" title="InstanceDisplayNamePrefix">InstanceDisplayNamePrefix</a>" : <i>String</i>,
        "<a href="#ishcxenabled" title="IsHcxEnabled">IsHcxEnabled</a>" : <i>Boolean</i>,
        "<a href="#nsxedgeuplink1vlanid" title="NsxEdgeUplink1vlanId">NsxEdgeUplink1vlanId</a>" : <i>String</i>,
        "<a href="#nsxedgeuplink2vlanid" title="NsxEdgeUplink2vlanId">NsxEdgeUplink2vlanId</a>" : <i>String</i>,
        "<a href="#nsxedgevtepvlanid" title="NsxEdgeVtepVlanId">NsxEdgeVtepVlanId</a>" : <i>String</i>,
        "<a href="#nsxvtepvlanid" title="NsxVtepVlanId">NsxVtepVlanId</a>" : <i>String</i>,
        "<a href="#provisioningsubnetid" title="ProvisioningSubnetId">ProvisioningSubnetId</a>" : <i>String</i>,
        "<a href="#provisioningvlanid" title="ProvisioningVlanId">ProvisioningVlanId</a>" : <i>String</i>,
        "<a href="#refreshhcxlicensestatus" title="RefreshHcxLicenseStatus">RefreshHcxLicenseStatus</a>" : <i>Boolean</i>,
        "<a href="#replicationvlanid" title="ReplicationVlanId">ReplicationVlanId</a>" : <i>String</i>,
        "<a href="#reservinghcxonpremiselicensekeys" title="ReservingHcxOnPremiseLicenseKeys">ReservingHcxOnPremiseLicenseKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#sshauthorizedkeys" title="SshAuthorizedKeys">SshAuthorizedKeys</a>" : <i>String</i>,
        "<a href="#vmotionvlanid" title="VmotionVlanId">VmotionVlanId</a>" : <i>String</i>,
        "<a href="#vmwaresoftwareversion" title="VmwareSoftwareVersion">VmwareSoftwareVersion</a>" : <i>String</i>,
        "<a href="#vsanvlanid" title="VsanVlanId">VsanVlanId</a>" : <i>String</i>,
        "<a href="#vspherevlanid" title="VsphereVlanId">VsphereVlanId</a>" : <i>String</i>,
        "<a href="#workloadnetworkcidr" title="WorkloadNetworkCidr">WorkloadNetworkCidr</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::OcvpSddc
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#computeavailabilitydomain" title="ComputeAvailabilityDomain">ComputeAvailabilityDomain</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#esxihostscount" title="EsxiHostsCount">EsxiHostsCount</a>: <i>Double</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#hcxaction" title="HcxAction">HcxAction</a>: <i>String</i>
    <a href="#hcxvlanid" title="HcxVlanId">HcxVlanId</a>: <i>String</i>
    <a href="#initialsku" title="InitialSku">InitialSku</a>: <i>String</i>
    <a href="#instancedisplaynameprefix" title="InstanceDisplayNamePrefix">InstanceDisplayNamePrefix</a>: <i>String</i>
    <a href="#ishcxenabled" title="IsHcxEnabled">IsHcxEnabled</a>: <i>Boolean</i>
    <a href="#nsxedgeuplink1vlanid" title="NsxEdgeUplink1vlanId">NsxEdgeUplink1vlanId</a>: <i>String</i>
    <a href="#nsxedgeuplink2vlanid" title="NsxEdgeUplink2vlanId">NsxEdgeUplink2vlanId</a>: <i>String</i>
    <a href="#nsxedgevtepvlanid" title="NsxEdgeVtepVlanId">NsxEdgeVtepVlanId</a>: <i>String</i>
    <a href="#nsxvtepvlanid" title="NsxVtepVlanId">NsxVtepVlanId</a>: <i>String</i>
    <a href="#provisioningsubnetid" title="ProvisioningSubnetId">ProvisioningSubnetId</a>: <i>String</i>
    <a href="#provisioningvlanid" title="ProvisioningVlanId">ProvisioningVlanId</a>: <i>String</i>
    <a href="#refreshhcxlicensestatus" title="RefreshHcxLicenseStatus">RefreshHcxLicenseStatus</a>: <i>Boolean</i>
    <a href="#replicationvlanid" title="ReplicationVlanId">ReplicationVlanId</a>: <i>String</i>
    <a href="#reservinghcxonpremiselicensekeys" title="ReservingHcxOnPremiseLicenseKeys">ReservingHcxOnPremiseLicenseKeys</a>: <i>
      - String</i>
    <a href="#sshauthorizedkeys" title="SshAuthorizedKeys">SshAuthorizedKeys</a>: <i>String</i>
    <a href="#vmotionvlanid" title="VmotionVlanId">VmotionVlanId</a>: <i>String</i>
    <a href="#vmwaresoftwareversion" title="VmwareSoftwareVersion">VmwareSoftwareVersion</a>: <i>String</i>
    <a href="#vsanvlanid" title="VsanVlanId">VsanVlanId</a>: <i>String</i>
    <a href="#vspherevlanid" title="VsphereVlanId">VsphereVlanId</a>: <i>String</i>
    <a href="#workloadnetworkcidr" title="WorkloadNetworkCidr">WorkloadNetworkCidr</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the SDDC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeAvailabilityDomain

The availability domain to create the SDDC's ESXi hosts in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A descriptive name for the SDDC. SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EsxiHostsCount

The number of ESXi hosts to create in the SDDC. You can add more hosts later (see [CreateEsxiHost](https://docs.cloud.oracle.com/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HcxAction

(Updatable) The action to be performed upon HCX licenses. "UPGRADE" will upgrade the SDDC from HCX Advanced to HCX Enterprise. "DOWNGRADE" will downgrade the SDDC from HCX Enterprise to HCX Advanced after current HCX Enterprise billing cycle end date. "CANCEL_DOWNGRADE" will cancel the pending downgrade of HCX licenses. The action will only be performed when its value is changed. This field can also be used to enable HCX Enterprise during SDDC creation. If "UPGRADE" is set during SDDC creation, the SDDC will be created with HCX Enterprise enable. Supported actions during update: UPGRADE, DOWNGRADE, CANCEL_DOWNGRADE. Supported actions during creation: UPGRADE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HcxVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the HCX component of the VMware environment. This value is required only when `isHcxEnabled` is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialSku

Billing option selected during SDDC creation. Oracle Cloud Infrastructure VMware Solution supports the following billing interval SKUs: HOUR, MONTH, ONE_YEAR, and THREE_YEARS. [ListSupportedSkus](https://docs.cloud.oracle.com/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceDisplayNamePrefix

A prefix used in the name of each ESXi host and Compute instance in the SDDC. If this isn't set, the SDDC's `displayName` is used as the prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHcxEnabled

Indicates whether to enable HCX for this SDDC.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxEdgeUplink1vlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the NSX Edge Uplink 1 component of the VMware environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxEdgeUplink2vlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the NSX Edge Uplink 2 component of the VMware environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxEdgeVtepVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the NSX Edge VTEP component of the VMware environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxVtepVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the NSX VTEP component of the VMware environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisioningSubnetId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management subnet to use for provisioning the SDDC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisioningVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC for the Provisioning component of the VMware environment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshHcxLicenseStatus

(Updatable) HCX on-premise licenses status will be refreshed whenever the value of this field is changed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC for the vSphere Replication component of the VMware environment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservingHcxOnPremiseLicenseKeys

(Updatable) The HCX on-premise licenses to be reserved when downgrade from HCX Enterprise to HCX Advanced. It should not be provided during resource creation. It is required and can only be set when the hcx_action is "DOWNGRADE". Its value can only be changed when hcx_action is updated.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAuthorizedKeys

(Updatable) One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmotionVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the vMotion component of the VMware environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmwareSoftwareVersion

(Updatable) The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use [ListSupportedVmwareSoftwareVersions](https://docs.cloud.oracle.com/iaas/api/#/en/vmware/20200501/SupportedVmwareSoftwareVersionSummary/ListSupportedVmwareSoftwareVersions).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsanVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the vSAN component of the VMware environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVlanId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN to use for the vSphere component of the VMware environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadNetworkCidr

The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application workloads.

_Required_: No

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

#### ActualEsxiHostsCount

Returns the <code>ActualEsxiHostsCount</code> value.

#### HcxFqdn

Returns the <code>HcxFqdn</code> value.

#### HcxInitialPassword

Returns the <code>HcxInitialPassword</code> value.

#### HcxOnPremKey

Returns the <code>HcxOnPremKey</code> value.

#### HcxOnPremLicenses

Returns the <code>HcxOnPremLicenses</code> value.

#### HcxPrivateIpId

Returns the <code>HcxPrivateIpId</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsHcxEnterpriseEnabled

Returns the <code>IsHcxEnterpriseEnabled</code> value.

#### IsHcxPendingDowngrade

Returns the <code>IsHcxPendingDowngrade</code> value.

#### NsxEdgeUplinkIpId

Returns the <code>NsxEdgeUplinkIpId</code> value.

#### NsxManagerFqdn

Returns the <code>NsxManagerFqdn</code> value.

#### NsxManagerInitialPassword

Returns the <code>NsxManagerInitialPassword</code> value.

#### NsxManagerPrivateIpId

Returns the <code>NsxManagerPrivateIpId</code> value.

#### NsxManagerUsername

Returns the <code>NsxManagerUsername</code> value.

#### NsxOverlaySegmentName

Returns the <code>NsxOverlaySegmentName</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeHcxBillingCycleEnd

Returns the <code>TimeHcxBillingCycleEnd</code> value.

#### TimeHcxLicenseStatusUpdated

Returns the <code>TimeHcxLicenseStatusUpdated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

#### VcenterFqdn

Returns the <code>VcenterFqdn</code> value.

#### VcenterInitialPassword

Returns the <code>VcenterInitialPassword</code> value.

#### VcenterPrivateIpId

Returns the <code>VcenterPrivateIpId</code> value.

#### VcenterUsername

Returns the <code>VcenterUsername</code> value.

