# Terraform::NS1::Zone

CloudFormation equivalent of ns1_zone

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NS1::Zone",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#additionalprimaries" title="AdditionalPrimaries">AdditionalPrimaries</a>" : <i>[ String, ... ]</i>,
        "<a href="#autogeneratensrecord" title="AutogenerateNsRecord">AutogenerateNsRecord</a>" : <i>Boolean</i>,
        "<a href="#dnsservers" title="DnsServers">DnsServers</a>" : <i>String</i>,
        "<a href="#dnssec" title="Dnssec">Dnssec</a>" : <i>Boolean</i>,
        "<a href="#expiry" title="Expiry">Expiry</a>" : <i>Double</i>,
        "<a href="#hostmaster" title="Hostmaster">Hostmaster</a>" : <i>String</i>,
        "<a href="#link" title="Link">Link</a>" : <i>String</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ Double, ... ]</i>,
        "<a href="#nxttl" title="NxTtl">NxTtl</a>" : <i>Double</i>,
        "<a href="#primary" title="Primary">Primary</a>" : <i>String</i>,
        "<a href="#refresh" title="Refresh">Refresh</a>" : <i>Double</i>,
        "<a href="#retry" title="Retry">Retry</a>" : <i>Double</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#secondaries" title="Secondaries">Secondaries</a>" : <i>[ &lt;a href=&#34;secondaries.md&#34;&gt;Secondaries&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NS1::Zone
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#additionalprimaries" title="AdditionalPrimaries">AdditionalPrimaries</a>: <i>
      - String</i>
    <a href="#autogeneratensrecord" title="AutogenerateNsRecord">AutogenerateNsRecord</a>: <i>Boolean</i>
    <a href="#dnsservers" title="DnsServers">DnsServers</a>: <i>String</i>
    <a href="#dnssec" title="Dnssec">Dnssec</a>: <i>Boolean</i>
    <a href="#expiry" title="Expiry">Expiry</a>: <i>Double</i>
    <a href="#hostmaster" title="Hostmaster">Hostmaster</a>: <i>String</i>
    <a href="#link" title="Link">Link</a>: <i>String</i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - Double</i>
    <a href="#nxttl" title="NxTtl">NxTtl</a>: <i>Double</i>
    <a href="#primary" title="Primary">Primary</a>: <i>String</i>
    <a href="#refresh" title="Refresh">Refresh</a>: <i>Double</i>
    <a href="#retry" title="Retry">Retry</a>: <i>Double</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#secondaries" title="Secondaries">Secondaries</a>: <i>
      - &lt;a href=&#34;secondaries.md&#34;&gt;Secondaries&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalPrimaries

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutogenerateNsRecord

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dnssec

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostmaster

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Link

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Refresh

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secondaries

_Required_: No

_Type_: List of &lt;a href=&#34;secondaries.md&#34;&gt;Secondaries&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DnsServers

Returns the &lt;code&gt;DnsServers&lt;/code&gt; value.

#### Hostmaster

Returns the &lt;code&gt;Hostmaster&lt;/code&gt; value.

