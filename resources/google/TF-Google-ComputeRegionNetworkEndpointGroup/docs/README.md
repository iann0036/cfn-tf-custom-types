# TF::Google::ComputeRegionNetworkEndpointGroup

A regional NEG that can support Serverless Products.

Recreating a region network endpoint group that's in use by another resource will give a
`resourceInUseByAnotherResource` error. Use `lifecycle.create_before_destroy`
to avoid this type of error.


To get more information about RegionNetworkEndpointGroup, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/regionNetworkEndpointGroups)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=region_network_endpoint_group_functions&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img al...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ComputeRegionNetworkEndpointGroup",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkendpointtype" title="NetworkEndpointType">NetworkEndpointType</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#appengine" title="AppEngine">AppEngine</a>" : <i>[ <a href="appenginedefinition.md">AppEngineDefinition</a>, ... ]</i>,
        "<a href="#cloudfunction" title="CloudFunction">CloudFunction</a>" : <i>[ <a href="cloudfunctiondefinition.md">CloudFunctionDefinition</a>, ... ]</i>,
        "<a href="#cloudrun" title="CloudRun">CloudRun</a>" : <i>[ <a href="cloudrundefinition.md">CloudRunDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ComputeRegionNetworkEndpointGroup
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkendpointtype" title="NetworkEndpointType">NetworkEndpointType</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#appengine" title="AppEngine">AppEngine</a>: <i>
      - <a href="appenginedefinition.md">AppEngineDefinition</a></i>
    <a href="#cloudfunction" title="CloudFunction">CloudFunction</a>: <i>
      - <a href="cloudfunctiondefinition.md">CloudFunctionDefinition</a></i>
    <a href="#cloudrun" title="CloudRun">CloudRun</a>: <i>
      - <a href="cloudrundefinition.md">CloudRunDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkEndpointType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppEngine

_Required_: No

_Type_: List of <a href="appenginedefinition.md">AppEngineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudFunction

_Required_: No

_Type_: List of <a href="cloudfunctiondefinition.md">CloudFunctionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRun

_Required_: No

_Type_: List of <a href="cloudrundefinition.md">CloudRunDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.
