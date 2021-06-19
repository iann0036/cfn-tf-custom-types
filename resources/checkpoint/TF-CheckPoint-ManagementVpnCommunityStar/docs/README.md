# TF::CheckPoint::ManagementVpnCommunityStar

This resource allows you to execute Check Point Vpn Community Star.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementVpnCommunityStar",
    "Properties" : {
        "<a href="#centergateways" title="CenterGateways">CenterGateways</a>" : <i>[ String, ... ]</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#encryptionmethod" title="EncryptionMethod">EncryptionMethod</a>" : <i>String</i>,
        "<a href="#encryptionsuite" title="EncryptionSuite">EncryptionSuite</a>" : <i>String</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#ikephase1" title="IkePhase1">IkePhase1</a>" : <i>[ <a href="ikephase1definition.md">IkePhase1Definition</a>, ... ]</i>,
        "<a href="#ikephase2" title="IkePhase2">IkePhase2</a>" : <i>[ <a href="ikephase2definition.md">IkePhase2Definition</a>, ... ]</i>,
        "<a href="#meshcentergateways" title="MeshCenterGateways">MeshCenterGateways</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#satellitegateways" title="SatelliteGateways">SatelliteGateways</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#usesharedsecret" title="UseSharedSecret">UseSharedSecret</a>" : <i>Boolean</i>,
        "<a href="#overridevpndomains" title="OverrideVpnDomains">OverrideVpnDomains</a>" : <i>[ <a href="overridevpndomainsdefinition.md">OverrideVpnDomainsDefinition</a>, ... ]</i>,
        "<a href="#sharedsecrets" title="SharedSecrets">SharedSecrets</a>" : <i>[ <a href="sharedsecretsdefinition.md">SharedSecretsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementVpnCommunityStar
Properties:
    <a href="#centergateways" title="CenterGateways">CenterGateways</a>: <i>
      - String</i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#encryptionmethod" title="EncryptionMethod">EncryptionMethod</a>: <i>String</i>
    <a href="#encryptionsuite" title="EncryptionSuite">EncryptionSuite</a>: <i>String</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#ikephase1" title="IkePhase1">IkePhase1</a>: <i>
      - <a href="ikephase1definition.md">IkePhase1Definition</a></i>
    <a href="#ikephase2" title="IkePhase2">IkePhase2</a>: <i>
      - <a href="ikephase2definition.md">IkePhase2Definition</a></i>
    <a href="#meshcentergateways" title="MeshCenterGateways">MeshCenterGateways</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#satellitegateways" title="SatelliteGateways">SatelliteGateways</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#usesharedsecret" title="UseSharedSecret">UseSharedSecret</a>: <i>Boolean</i>
    <a href="#overridevpndomains" title="OverrideVpnDomains">OverrideVpnDomains</a>: <i>
      - <a href="overridevpndomainsdefinition.md">OverrideVpnDomainsDefinition</a></i>
    <a href="#sharedsecrets" title="SharedSecrets">SharedSecrets</a>: <i>
      - <a href="sharedsecretsdefinition.md">SharedSecretsDefinition</a></i>
</pre>

## Properties

#### CenterGateways

Collection of Gateway objects representing center gateways identified by the name or UID.center_gateways blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of the object. Should be one of existing colors.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionMethod

The encryption method to be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionSuite

The encryption suite to be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreErrors

Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreWarnings

Apply changes ignoring warnings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkePhase1

Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom].ike_phase_1 blocks are documented below.

_Required_: No

_Type_: List of <a href="ikephase1definition.md">IkePhase1Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkePhase2

Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom].ike_phase_2 blocks are documented below.

_Required_: No

_Type_: List of <a href="ikephase2definition.md">IkePhase2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshCenterGateways

Indicates whether the meshed community is in center.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatelliteGateways

Collection of Gateway objects representing satellite gateways identified by the name or UID.satellite_gateways blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tag identifiers.tags blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSharedSecret

Indicates whether the shared secret should be used for all external gateways.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideVpnDomains

_Required_: No

_Type_: List of <a href="overridevpndomainsdefinition.md">OverrideVpnDomainsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedSecrets

_Required_: No

_Type_: List of <a href="sharedsecretsdefinition.md">SharedSecretsDefinition</a>

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

