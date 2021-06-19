# TF::Rancher2::GlobalDnsProvider

Provides a Rancher V2 Global DNS Provider resource. This can be used to create Global DNS Providers for Rancher V2. Supported Global DNS Providers: `alidns, cloudflare, route53`

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::GlobalDnsProvider",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rootdomain" title="RootDomain">RootDomain</a>" : <i>String</i>,
        "<a href="#alidnsconfig" title="AlidnsConfig">AlidnsConfig</a>" : <i>[ <a href="alidnsconfigdefinition.md">AlidnsConfigDefinition</a>, ... ]</i>,
        "<a href="#cloudflareconfig" title="CloudflareConfig">CloudflareConfig</a>" : <i>[ <a href="cloudflareconfigdefinition.md">CloudflareConfigDefinition</a>, ... ]</i>,
        "<a href="#route53config" title="Route53Config">Route53Config</a>" : <i>[ <a href="route53configdefinition.md">Route53ConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::GlobalDnsProvider
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rootdomain" title="RootDomain">RootDomain</a>: <i>String</i>
    <a href="#alidnsconfig" title="AlidnsConfig">AlidnsConfig</a>: <i>
      - <a href="alidnsconfigdefinition.md">AlidnsConfigDefinition</a></i>
    <a href="#cloudflareconfig" title="CloudflareConfig">CloudflareConfig</a>: <i>
      - <a href="cloudflareconfigdefinition.md">CloudflareConfigDefinition</a></i>
    <a href="#route53config" title="Route53Config">Route53Config</a>: <i>
      - <a href="route53configdefinition.md">Route53ConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Annotations

Annotations for Global DNS Provider (map).

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Labels for Global DNS Provider (map).

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Global DNS Provider (string).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDomain

The user ID to assign Global DNS Provider (string).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlidnsConfig

_Required_: No

_Type_: List of <a href="alidnsconfigdefinition.md">AlidnsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudflareConfig

_Required_: No

_Type_: List of <a href="cloudflareconfigdefinition.md">CloudflareConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route53Config

_Required_: No

_Type_: List of <a href="route53configdefinition.md">Route53ConfigDefinition</a>

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

#### DnsProvider

Returns the <code>DnsProvider</code> value.

#### Id

Returns the <code>Id</code> value.

