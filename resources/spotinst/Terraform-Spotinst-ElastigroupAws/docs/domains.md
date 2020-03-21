# Terraform::Spotinst::ElastigroupAws Domains

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>" : <i>String</i>,
    "<a href="#spotinstacctid" title="SpotinstAcctId">SpotinstAcctId</a>" : <i>String</i>,
    "<a href="#recordsets" title="RecordSets">RecordSets</a>" : <i>[ <a href="domains-recordsets.md">RecordSets</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>: <i>String</i>
<a href="#spotinstacctid" title="SpotinstAcctId">SpotinstAcctId</a>: <i>String</i>
<a href="#recordsets" title="RecordSets">RecordSets</a>: <i>
      - <a href="domains-recordsets.md">RecordSets</a></i>
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
_Type_: List of <a href="domains-recordsets.md">RecordSets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

