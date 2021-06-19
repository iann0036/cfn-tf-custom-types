# TF::Volterra::Bgp InternalDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#disablemtls" title="DisableMtls">DisableMtls</a>" : <i>Boolean</i>,
    "<a href="#dnsname" title="DnsName">DnsName</a>" : <i>String</i>,
    "<a href="#enablemtls" title="EnableMtls">EnableMtls</a>" : <i>Boolean</i>,
    "<a href="#fromsite" title="FromSite">FromSite</a>" : <i>Boolean</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#familyinet6vpn" title="FamilyInet6vpn">FamilyInet6vpn</a>" : <i>[ <a href="familyinet6vpndefinition.md">FamilyInet6vpnDefinition</a>, ... ]</i>,
    "<a href="#familyinetvpn" title="FamilyInetvpn">FamilyInetvpn</a>" : <i>[ <a href="familyinetvpndefinition.md">FamilyInetvpnDefinition</a>, ... ]</i>,
    "<a href="#familyrtarget" title="FamilyRtarget">FamilyRtarget</a>" : <i>[ <a href="familyrtargetdefinition.md">FamilyRtargetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#disablemtls" title="DisableMtls">DisableMtls</a>: <i>Boolean</i>
<a href="#dnsname" title="DnsName">DnsName</a>: <i>String</i>
<a href="#enablemtls" title="EnableMtls">EnableMtls</a>: <i>Boolean</i>
<a href="#fromsite" title="FromSite">FromSite</a>: <i>Boolean</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#familyinet6vpn" title="FamilyInet6vpn">FamilyInet6vpn</a>: <i>
      - <a href="familyinet6vpndefinition.md">FamilyInet6vpnDefinition</a></i>
<a href="#familyinetvpn" title="FamilyInetvpn">FamilyInetvpn</a>: <i>
      - <a href="familyinetvpndefinition.md">FamilyInetvpnDefinition</a></i>
<a href="#familyrtarget" title="FamilyRtarget">FamilyRtarget</a>: <i>
      - <a href="familyrtargetdefinition.md">FamilyRtargetDefinition</a></i>
</pre>

## Properties

#### Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableMtls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMtls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromSite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FamilyInet6vpn

_Required_: No

_Type_: List of <a href="familyinet6vpndefinition.md">FamilyInet6vpnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FamilyInetvpn

_Required_: No

_Type_: List of <a href="familyinetvpndefinition.md">FamilyInetvpnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FamilyRtarget

_Required_: No

_Type_: List of <a href="familyrtargetdefinition.md">FamilyRtargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

