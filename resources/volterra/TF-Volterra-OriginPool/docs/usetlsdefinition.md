# TF::Volterra::OriginPool UseTlsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablesni" title="DisableSni">DisableSni</a>" : <i>Boolean</i>,
    "<a href="#nomtls" title="NoMtls">NoMtls</a>" : <i>Boolean</i>,
    "<a href="#skipserververification" title="SkipServerVerification">SkipServerVerification</a>" : <i>Boolean</i>,
    "<a href="#sni" title="Sni">Sni</a>" : <i>String</i>,
    "<a href="#usehostheaderassni" title="UseHostHeaderAsSni">UseHostHeaderAsSni</a>" : <i>Boolean</i>,
    "<a href="#volterratrustedca" title="VolterraTrustedCa">VolterraTrustedCa</a>" : <i>Boolean</i>,
    "<a href="#tlsconfig" title="TlsConfig">TlsConfig</a>" : <i>[ <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>, ... ]</i>,
    "<a href="#usemtls" title="UseMtls">UseMtls</a>" : <i>[ <a href="usemtlsdefinition.md">UseMtlsDefinition</a>, ... ]</i>,
    "<a href="#useserververification" title="UseServerVerification">UseServerVerification</a>" : <i>[ <a href="useserververificationdefinition.md">UseServerVerificationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablesni" title="DisableSni">DisableSni</a>: <i>Boolean</i>
<a href="#nomtls" title="NoMtls">NoMtls</a>: <i>Boolean</i>
<a href="#skipserververification" title="SkipServerVerification">SkipServerVerification</a>: <i>Boolean</i>
<a href="#sni" title="Sni">Sni</a>: <i>String</i>
<a href="#usehostheaderassni" title="UseHostHeaderAsSni">UseHostHeaderAsSni</a>: <i>Boolean</i>
<a href="#volterratrustedca" title="VolterraTrustedCa">VolterraTrustedCa</a>: <i>Boolean</i>
<a href="#tlsconfig" title="TlsConfig">TlsConfig</a>: <i>
      - <a href="tlsconfigdefinition.md">TlsConfigDefinition</a></i>
<a href="#usemtls" title="UseMtls">UseMtls</a>: <i>
      - <a href="usemtlsdefinition.md">UseMtlsDefinition</a></i>
<a href="#useserververification" title="UseServerVerification">UseServerVerification</a>: <i>
      - <a href="useserververificationdefinition.md">UseServerVerificationDefinition</a></i>
</pre>

## Properties

#### DisableSni

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoMtls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipServerVerification

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sni

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseHostHeaderAsSni

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolterraTrustedCa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsConfig

_Required_: No

_Type_: List of <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMtls

_Required_: No

_Type_: List of <a href="usemtlsdefinition.md">UseMtlsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseServerVerification

_Required_: No

_Type_: List of <a href="useserververificationdefinition.md">UseServerVerificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

