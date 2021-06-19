# TF::AVI::Licenseledgerdetails

The LicenseLedgerDetails resource allows the creation and management of Avi LicenseLedgerDetails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Licenseledgerdetails",
    "Properties" : {
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#escrowinfos" title="EscrowInfos">EscrowInfos</a>" : <i>[ <a href="escrowinfosdefinition.md">EscrowInfosDefinition</a>, ... ]</i>,
        "<a href="#seinfos" title="SeInfos">SeInfos</a>" : <i>[ <a href="seinfosdefinition.md">SeInfosDefinition</a>, ... ]</i>,
        "<a href="#tierusages" title="TierUsages">TierUsages</a>" : <i>[ <a href="tierusagesdefinition.md">TierUsagesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Licenseledgerdetails
Properties:
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#escrowinfos" title="EscrowInfos">EscrowInfos</a>: <i>
      - <a href="escrowinfosdefinition.md">EscrowInfosDefinition</a></i>
    <a href="#seinfos" title="SeInfos">SeInfos</a>: <i>
      - <a href="seinfosdefinition.md">SeInfosDefinition</a></i>
    <a href="#tierusages" title="TierUsages">TierUsages</a>: <i>
      - <a href="tierusagesdefinition.md">TierUsagesDefinition</a></i>
</pre>

## Properties

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscrowInfos

_Required_: No

_Type_: List of <a href="escrowinfosdefinition.md">EscrowInfosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeInfos

_Required_: No

_Type_: List of <a href="seinfosdefinition.md">SeInfosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TierUsages

_Required_: No

_Type_: List of <a href="tierusagesdefinition.md">TierUsagesDefinition</a>

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

