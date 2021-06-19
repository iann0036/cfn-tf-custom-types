# TF::AVI::Vsvip DnsInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
    "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
    "<a href="#numrecordsinresponse" title="NumRecordsInResponse">NumRecordsInResponse</a>" : <i>Double</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#cname" title="Cname">Cname</a>" : <i>[ <a href="cnamedefinition.md">CnameDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
<a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
<a href="#numrecordsinresponse" title="NumRecordsInResponse">NumRecordsInResponse</a>: <i>Double</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#cname" title="Cname">Cname</a>: <i>
      - <a href="cnamedefinition.md">CnameDefinition</a></i>
</pre>

## Properties

#### Algorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumRecordsInResponse

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cname

_Required_: No

_Type_: List of <a href="cnamedefinition.md">CnameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

