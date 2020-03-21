# Terraform::AWS::ServiceDiscoveryService

CloudFormation equivalent of aws_service_discovery_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ServiceDiscoveryService",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespaceid" title="NamespaceId">NamespaceId</a>" : <i>String</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#healthcheckconfig" title="HealthCheckConfig">HealthCheckConfig</a>" : <i>[ &lt;a href=&#34;healthcheckconfig.md&#34;&gt;HealthCheckConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#healthcheckcustomconfig" title="HealthCheckCustomConfig">HealthCheckCustomConfig</a>" : <i>[ &lt;a href=&#34;healthcheckcustomconfig.md&#34;&gt;HealthCheckCustomConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#dnsrecords" title="DnsRecords">DnsRecords</a>" : <i>[ &lt;a href=&#34;dnsrecords.md&#34;&gt;DnsRecords&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ServiceDiscoveryService
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespaceid" title="NamespaceId">NamespaceId</a>: <i>String</i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;</i>
    <a href="#healthcheckconfig" title="HealthCheckConfig">HealthCheckConfig</a>: <i>
      - &lt;a href=&#34;healthcheckconfig.md&#34;&gt;HealthCheckConfig&lt;/a&gt;</i>
    <a href="#healthcheckcustomconfig" title="HealthCheckCustomConfig">HealthCheckCustomConfig</a>: <i>
      - &lt;a href=&#34;healthcheckcustomconfig.md&#34;&gt;HealthCheckCustomConfig&lt;/a&gt;</i>
    <a href="#dnsrecords" title="DnsRecords">DnsRecords</a>: <i>
      - &lt;a href=&#34;dnsrecords.md&#34;&gt;DnsRecords&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckConfig

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheckconfig.md&#34;&gt;HealthCheckConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckCustomConfig

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheckcustomconfig.md&#34;&gt;HealthCheckCustomConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsRecords

_Required_: No

_Type_: List of &lt;a href=&#34;dnsrecords.md&#34;&gt;DnsRecords&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

