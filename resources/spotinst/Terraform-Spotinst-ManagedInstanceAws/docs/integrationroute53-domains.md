# Terraform::Spotinst::ManagedInstanceAws IntegrationRoute53 Domains

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>" : <i>String</i>,
    "<a href="#spotinstacctid" title="SpotinstAcctId">SpotinstAcctId</a>" : <i>String</i>,
    "<a href="#recordsets" title="RecordSets">RecordSets</a>" : <i>[ &lt;a href=&#34;integrationroute53-domains-recordsets.md&#34;&gt;RecordSets&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>: <i>String</i>
<a href="#spotinstacctid" title="SpotinstAcctId">SpotinstAcctId</a>: <i>String</i>
<a href="#recordsets" title="RecordSets">RecordSets</a>: <i>
      - &lt;a href=&#34;integrationroute53-domains-recordsets.md&#34;&gt;RecordSets&lt;/a&gt;</i>
</pre>

## Properties

#### HostedZoneId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotinstAcctId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordSets

_Required_: No
_Type_: List of &lt;a href=&#34;integrationroute53-domains-recordsets.md&#34;&gt;RecordSets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

