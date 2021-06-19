# TF::AWS::AppmeshVirtualNode VirtualServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#virtualservicename" title="VirtualServiceName">VirtualServiceName</a>" : <i>String</i>,
    "<a href="#clientpolicy" title="ClientPolicy">ClientPolicy</a>" : <i>[ <a href="clientpolicydefinition.md">ClientPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#virtualservicename" title="VirtualServiceName">VirtualServiceName</a>: <i>String</i>
<a href="#clientpolicy" title="ClientPolicy">ClientPolicy</a>: <i>
      - <a href="clientpolicydefinition.md">ClientPolicyDefinition</a></i>
</pre>

## Properties

#### VirtualServiceName

The name of the virtual service that is acting as a virtual node backend. Must be between 1 and 255 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientPolicy

_Required_: No

_Type_: List of <a href="clientpolicydefinition.md">ClientPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

