# TF::BIGIP::EventServiceDiscovery

`bigip_event_service_discovery` Terraform resource to update pool members based on event driven Service Discovery.

The API endpoint for Service discovery tasks should be available before using the resource and with this resource,we will be able to connect to a specific endpoint related to event based service discovery that will allow us to update the list of pool members

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::EventServiceDiscovery",
    "Properties" : {
        "<a href="#taskid" title="Taskid">Taskid</a>" : <i>String</i>,
        "<a href="#node" title="Node">Node</a>" : <i>[ <a href="nodedefinition.md">NodeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::EventServiceDiscovery
Properties:
    <a href="#taskid" title="Taskid">Taskid</a>: <i>String</i>
    <a href="#node" title="Node">Node</a>: <i>
      - <a href="nodedefinition.md">NodeDefinition</a></i>
</pre>

## Properties

#### Taskid

servicediscovery endpoint ( Below example shows how to create endpoing using AS3 ).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node

_Required_: No

_Type_: List of <a href="nodedefinition.md">NodeDefinition</a>

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

