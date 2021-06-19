# TF::Rancher2::Cluster OpenstackCloudProviderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blockstorage" title="BlockStorage">BlockStorage</a>" : <i>[ <a href="blockstoragedefinition.md">BlockStorageDefinition</a>, ... ]</i>,
    "<a href="#global" title="Global">Global</a>" : <i>[ <a href="globaldefinition.md">GlobalDefinition</a>, ... ]</i>,
    "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>[ <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>, ... ]</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
    "<a href="#route" title="Route">Route</a>" : <i>[ <a href="routedefinition.md">RouteDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#blockstorage" title="BlockStorage">BlockStorage</a>: <i>
      - <a href="blockstoragedefinition.md">BlockStorageDefinition</a></i>
<a href="#global" title="Global">Global</a>: <i>
      - <a href="globaldefinition.md">GlobalDefinition</a></i>
<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>
      - <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a></i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
<a href="#route" title="Route">Route</a>: <i>
      - <a href="routedefinition.md">RouteDefinition</a></i>
</pre>

## Properties

#### BlockStorage

_Required_: No

_Type_: List of <a href="blockstoragedefinition.md">BlockStorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Global

_Required_: No

_Type_: List of <a href="globaldefinition.md">GlobalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: No

_Type_: List of <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of <a href="routedefinition.md">RouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

