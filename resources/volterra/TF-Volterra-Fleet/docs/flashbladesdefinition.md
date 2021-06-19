# TF::Volterra::Fleet FlashBladesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#lables" title="Lables">Lables</a>" : <i>[ <a href="lablesdefinition.md">LablesDefinition</a>, ... ]</i>,
    "<a href="#mgmtdnsname" title="MgmtDnsName">MgmtDnsName</a>" : <i>String</i>,
    "<a href="#mgmtip" title="MgmtIp">MgmtIp</a>" : <i>String</i>,
    "<a href="#nfsendpointdnsname" title="NfsEndpointDnsName">NfsEndpointDnsName</a>" : <i>String</i>,
    "<a href="#nfsendpointip" title="NfsEndpointIp">NfsEndpointIp</a>" : <i>String</i>,
    "<a href="#apitoken" title="ApiToken">ApiToken</a>" : <i>[ <a href="apitokendefinition.md">ApiTokenDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#lables" title="Lables">Lables</a>: <i>
      - <a href="lablesdefinition.md">LablesDefinition</a></i>
<a href="#mgmtdnsname" title="MgmtDnsName">MgmtDnsName</a>: <i>String</i>
<a href="#mgmtip" title="MgmtIp">MgmtIp</a>: <i>String</i>
<a href="#nfsendpointdnsname" title="NfsEndpointDnsName">NfsEndpointDnsName</a>: <i>String</i>
<a href="#nfsendpointip" title="NfsEndpointIp">NfsEndpointIp</a>: <i>String</i>
<a href="#apitoken" title="ApiToken">ApiToken</a>: <i>
      - <a href="apitokendefinition.md">ApiTokenDefinition</a></i>
</pre>

## Properties

#### Lables

_Required_: No

_Type_: List of <a href="lablesdefinition.md">LablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtDnsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsEndpointDnsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsEndpointIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiToken

_Required_: No

_Type_: List of <a href="apitokendefinition.md">ApiTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

