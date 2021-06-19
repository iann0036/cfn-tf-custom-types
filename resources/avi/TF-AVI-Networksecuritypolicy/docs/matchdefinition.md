# TF::AVI::Networksecuritypolicy MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>[ <a href="clientipdefinition.md">ClientIpDefinition</a>, ... ]</i>,
    "<a href="#clientport" title="ClientPort">ClientPort</a>" : <i>[ <a href="clientportdefinition.md">ClientPortDefinition</a>, ... ]</i>,
    "<a href="#ipreputationtype" title="IpReputationType">IpReputationType</a>" : <i>[ <a href="ipreputationtypedefinition.md">IpReputationTypeDefinition</a>, ... ]</i>,
    "<a href="#microservice" title="Microservice">Microservice</a>" : <i>[ <a href="microservicedefinition.md">MicroserviceDefinition</a>, ... ]</i>,
    "<a href="#vsport" title="VsPort">VsPort</a>" : <i>[ <a href="vsportdefinition.md">VsPortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientip" title="ClientIp">ClientIp</a>: <i>
      - <a href="clientipdefinition.md">ClientIpDefinition</a></i>
<a href="#clientport" title="ClientPort">ClientPort</a>: <i>
      - <a href="clientportdefinition.md">ClientPortDefinition</a></i>
<a href="#ipreputationtype" title="IpReputationType">IpReputationType</a>: <i>
      - <a href="ipreputationtypedefinition.md">IpReputationTypeDefinition</a></i>
<a href="#microservice" title="Microservice">Microservice</a>: <i>
      - <a href="microservicedefinition.md">MicroserviceDefinition</a></i>
<a href="#vsport" title="VsPort">VsPort</a>: <i>
      - <a href="vsportdefinition.md">VsPortDefinition</a></i>
</pre>

## Properties

#### ClientIp

_Required_: No

_Type_: List of <a href="clientipdefinition.md">ClientIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientPort

_Required_: No

_Type_: List of <a href="clientportdefinition.md">ClientPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReputationType

_Required_: No

_Type_: List of <a href="ipreputationtypedefinition.md">IpReputationTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Microservice

_Required_: No

_Type_: List of <a href="microservicedefinition.md">MicroserviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsPort

_Required_: No

_Type_: List of <a href="vsportdefinition.md">VsPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

