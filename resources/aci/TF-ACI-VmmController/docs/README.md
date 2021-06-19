# TF::ACI::VmmController

CloudFormation equivalent of aci_vmm_controller

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::VmmController",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dvsversion" title="DvsVersion">DvsVersion</a>" : <i>String</i>,
        "<a href="#hostorip" title="HostOrIp">HostOrIp</a>" : <i>String</i>,
        "<a href="#inventorytrigst" title="InventoryTrigSt">InventoryTrigSt</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#msftconfigerrmsg" title="MsftConfigErrMsg">MsftConfigErrMsg</a>" : <i>String</i>,
        "<a href="#msftconfigissues" title="MsftConfigIssues">MsftConfigIssues</a>" : <i>[ String, ... ]</i>,
        "<a href="#n1kvstatsmode" title="N1kvStatsMode">N1kvStatsMode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#relationvmmrsacc" title="RelationVmmRsAcc">RelationVmmRsAcc</a>" : <i>String</i>,
        "<a href="#relationvmmrsctrlrpmonpol" title="RelationVmmRsCtrlrPMonPol">RelationVmmRsCtrlrPMonPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsmcastaddrns" title="RelationVmmRsMcastAddrNs">RelationVmmRsMcastAddrNs</a>" : <i>String</i>,
        "<a href="#relationvmmrsmgmtepg" title="RelationVmmRsMgmtEPg">RelationVmmRsMgmtEPg</a>" : <i>String</i>,
        "<a href="#relationvmmrstoextdevmgr" title="RelationVmmRsToExtDevMgr">RelationVmmRsToExtDevMgr</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationvmmrsvxlanns" title="RelationVmmRsVxlanNs">RelationVmmRsVxlanNs</a>" : <i>String</i>,
        "<a href="#relationvmmrsvxlannsdef" title="RelationVmmRsVxlanNsDef">RelationVmmRsVxlanNsDef</a>" : <i>String</i>,
        "<a href="#rootcontname" title="RootContName">RootContName</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#seqnum" title="SeqNum">SeqNum</a>" : <i>String</i>,
        "<a href="#statsmode" title="StatsMode">StatsMode</a>" : <i>String</i>,
        "<a href="#vmmdomaindn" title="VmmDomainDn">VmmDomainDn</a>" : <i>String</i>,
        "<a href="#vxlandeplpref" title="VxlanDeplPref">VxlanDeplPref</a>" : <i>String</i>,
        "<a href="#relationvmmrsvmmctrlrp" title="RelationVmmRsVmmCtrlrP">RelationVmmRsVmmCtrlrP</a>" : <i>[ <a href="relationvmmrsvmmctrlrpdefinition.md">RelationVmmRsVmmCtrlrPDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::VmmController
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dvsversion" title="DvsVersion">DvsVersion</a>: <i>String</i>
    <a href="#hostorip" title="HostOrIp">HostOrIp</a>: <i>String</i>
    <a href="#inventorytrigst" title="InventoryTrigSt">InventoryTrigSt</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#msftconfigerrmsg" title="MsftConfigErrMsg">MsftConfigErrMsg</a>: <i>String</i>
    <a href="#msftconfigissues" title="MsftConfigIssues">MsftConfigIssues</a>: <i>
      - String</i>
    <a href="#n1kvstatsmode" title="N1kvStatsMode">N1kvStatsMode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#relationvmmrsacc" title="RelationVmmRsAcc">RelationVmmRsAcc</a>: <i>String</i>
    <a href="#relationvmmrsctrlrpmonpol" title="RelationVmmRsCtrlrPMonPol">RelationVmmRsCtrlrPMonPol</a>: <i>String</i>
    <a href="#relationvmmrsmcastaddrns" title="RelationVmmRsMcastAddrNs">RelationVmmRsMcastAddrNs</a>: <i>String</i>
    <a href="#relationvmmrsmgmtepg" title="RelationVmmRsMgmtEPg">RelationVmmRsMgmtEPg</a>: <i>String</i>
    <a href="#relationvmmrstoextdevmgr" title="RelationVmmRsToExtDevMgr">RelationVmmRsToExtDevMgr</a>: <i>
      - String</i>
    <a href="#relationvmmrsvxlanns" title="RelationVmmRsVxlanNs">RelationVmmRsVxlanNs</a>: <i>String</i>
    <a href="#relationvmmrsvxlannsdef" title="RelationVmmRsVxlanNsDef">RelationVmmRsVxlanNsDef</a>: <i>String</i>
    <a href="#rootcontname" title="RootContName">RootContName</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#seqnum" title="SeqNum">SeqNum</a>: <i>String</i>
    <a href="#statsmode" title="StatsMode">StatsMode</a>: <i>String</i>
    <a href="#vmmdomaindn" title="VmmDomainDn">VmmDomainDn</a>: <i>String</i>
    <a href="#vxlandeplpref" title="VxlanDeplPref">VxlanDeplPref</a>: <i>String</i>
    <a href="#relationvmmrsvmmctrlrp" title="RelationVmmRsVmmCtrlrP">RelationVmmRsVmmCtrlrP</a>: <i>
      - <a href="relationvmmrsvmmctrlrpdefinition.md">RelationVmmRsVmmCtrlrPDefinition</a></i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DvsVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostOrIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InventoryTrigSt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MsftConfigErrMsg

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MsftConfigIssues

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### N1kvStatsMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsAcc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsCtrlrPMonPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsMcastAddrNs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsMgmtEPg

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsToExtDevMgr

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVxlanNs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVxlanNsDef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootContName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeqNum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmmDomainDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VxlanDeplPref

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVmmCtrlrP

_Required_: No

_Type_: List of <a href="relationvmmrsvmmctrlrpdefinition.md">RelationVmmRsVmmCtrlrPDefinition</a>

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

