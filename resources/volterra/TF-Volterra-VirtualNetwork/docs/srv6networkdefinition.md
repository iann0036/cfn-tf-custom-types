# TF::Volterra::VirtualNetwork Srv6NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#anycastvip" title="AnycastVip">AnycastVip</a>" : <i>String</i>,
    "<a href="#interfaceipsnatpool" title="InterfaceIpSnatPool">InterfaceIpSnatPool</a>" : <i>Boolean</i>,
    "<a href="#interfaceipvip" title="InterfaceIpVip">InterfaceIpVip</a>" : <i>Boolean</i>,
    "<a href="#nonamespacenetwork" title="NoNamespaceNetwork">NoNamespaceNetwork</a>" : <i>Boolean</i>,
    "<a href="#remotesidstatsplen" title="RemoteSidStatsPlen">RemoteSidStatsPlen</a>" : <i>Double</i>,
    "<a href="#accessnetworkrtargets" title="AccessNetworkRtargets">AccessNetworkRtargets</a>" : <i>[ <a href="accessnetworkrtargetsdefinition.md">AccessNetworkRtargetsDefinition</a>, ... ]</i>,
    "<a href="#enterprisenetworkrtargets" title="EnterpriseNetworkRtargets">EnterpriseNetworkRtargets</a>" : <i>[ <a href="enterprisenetworkrtargetsdefinition.md">EnterpriseNetworkRtargetsDefinition</a>, ... ]</i>,
    "<a href="#exportrtargets" title="ExportRtargets">ExportRtargets</a>" : <i>[ <a href="exportrtargetsdefinition.md">ExportRtargetsDefinition</a>, ... ]</i>,
    "<a href="#fleetsnatpool" title="FleetSnatPool">FleetSnatPool</a>" : <i>[ <a href="fleetsnatpooldefinition.md">FleetSnatPoolDefinition</a>, ... ]</i>,
    "<a href="#fleetvip" title="FleetVip">FleetVip</a>" : <i>[ <a href="fleetvipdefinition.md">FleetVipDefinition</a>, ... ]</i>,
    "<a href="#fleets" title="Fleets">Fleets</a>" : <i>[ <a href="fleetsdefinition.md">FleetsDefinition</a>, ... ]</i>,
    "<a href="#internetrtargets" title="InternetRtargets">InternetRtargets</a>" : <i>[ <a href="internetrtargetsdefinition.md">InternetRtargetsDefinition</a>, ... ]</i>,
    "<a href="#sitesnatpool" title="SiteSnatPool">SiteSnatPool</a>" : <i>[ <a href="sitesnatpooldefinition.md">SiteSnatPoolDefinition</a>, ... ]</i>,
    "<a href="#slice" title="Slice">Slice</a>" : <i>[ <a href="slicedefinition.md">SliceDefinition</a>, ... ]</i>,
    "<a href="#srv6networknsparams" title="Srv6NetworkNsParams">Srv6NetworkNsParams</a>" : <i>[ <a href="srv6networknsparamsdefinition.md">Srv6NetworkNsParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#anycastvip" title="AnycastVip">AnycastVip</a>: <i>String</i>
<a href="#interfaceipsnatpool" title="InterfaceIpSnatPool">InterfaceIpSnatPool</a>: <i>Boolean</i>
<a href="#interfaceipvip" title="InterfaceIpVip">InterfaceIpVip</a>: <i>Boolean</i>
<a href="#nonamespacenetwork" title="NoNamespaceNetwork">NoNamespaceNetwork</a>: <i>Boolean</i>
<a href="#remotesidstatsplen" title="RemoteSidStatsPlen">RemoteSidStatsPlen</a>: <i>Double</i>
<a href="#accessnetworkrtargets" title="AccessNetworkRtargets">AccessNetworkRtargets</a>: <i>
      - <a href="accessnetworkrtargetsdefinition.md">AccessNetworkRtargetsDefinition</a></i>
<a href="#enterprisenetworkrtargets" title="EnterpriseNetworkRtargets">EnterpriseNetworkRtargets</a>: <i>
      - <a href="enterprisenetworkrtargetsdefinition.md">EnterpriseNetworkRtargetsDefinition</a></i>
<a href="#exportrtargets" title="ExportRtargets">ExportRtargets</a>: <i>
      - <a href="exportrtargetsdefinition.md">ExportRtargetsDefinition</a></i>
<a href="#fleetsnatpool" title="FleetSnatPool">FleetSnatPool</a>: <i>
      - <a href="fleetsnatpooldefinition.md">FleetSnatPoolDefinition</a></i>
<a href="#fleetvip" title="FleetVip">FleetVip</a>: <i>
      - <a href="fleetvipdefinition.md">FleetVipDefinition</a></i>
<a href="#fleets" title="Fleets">Fleets</a>: <i>
      - <a href="fleetsdefinition.md">FleetsDefinition</a></i>
<a href="#internetrtargets" title="InternetRtargets">InternetRtargets</a>: <i>
      - <a href="internetrtargetsdefinition.md">InternetRtargetsDefinition</a></i>
<a href="#sitesnatpool" title="SiteSnatPool">SiteSnatPool</a>: <i>
      - <a href="sitesnatpooldefinition.md">SiteSnatPoolDefinition</a></i>
<a href="#slice" title="Slice">Slice</a>: <i>
      - <a href="slicedefinition.md">SliceDefinition</a></i>
<a href="#srv6networknsparams" title="Srv6NetworkNsParams">Srv6NetworkNsParams</a>: <i>
      - <a href="srv6networknsparamsdefinition.md">Srv6NetworkNsParamsDefinition</a></i>
</pre>

## Properties

#### AnycastVip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceIpSnatPool

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceIpVip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoNamespaceNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSidStatsPlen

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessNetworkRtargets

_Required_: No

_Type_: List of <a href="accessnetworkrtargetsdefinition.md">AccessNetworkRtargetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseNetworkRtargets

_Required_: No

_Type_: List of <a href="enterprisenetworkrtargetsdefinition.md">EnterpriseNetworkRtargetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportRtargets

_Required_: No

_Type_: List of <a href="exportrtargetsdefinition.md">ExportRtargetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetSnatPool

_Required_: No

_Type_: List of <a href="fleetsnatpooldefinition.md">FleetSnatPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetVip

_Required_: No

_Type_: List of <a href="fleetvipdefinition.md">FleetVipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fleets

_Required_: No

_Type_: List of <a href="fleetsdefinition.md">FleetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetRtargets

_Required_: No

_Type_: List of <a href="internetrtargetsdefinition.md">InternetRtargetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteSnatPool

_Required_: No

_Type_: List of <a href="sitesnatpooldefinition.md">SiteSnatPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slice

_Required_: No

_Type_: List of <a href="slicedefinition.md">SliceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srv6NetworkNsParams

_Required_: No

_Type_: List of <a href="srv6networknsparamsdefinition.md">Srv6NetworkNsParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

