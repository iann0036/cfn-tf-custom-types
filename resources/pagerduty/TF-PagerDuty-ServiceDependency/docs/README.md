# TF::PagerDuty::ServiceDependency

A [service dependency](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1service_dependencies~1associate/post) is a relationship between two services that this service uses, or that are used by this service, and are critical for successful operation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::ServiceDependency",
    "Properties" : {
        "<a href="#dependency" title="Dependency">Dependency</a>" : <i>[ <a href="dependencydefinition.md">DependencyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::ServiceDependency
Properties:
    <a href="#dependency" title="Dependency">Dependency</a>: <i>
      - <a href="dependencydefinition.md">DependencyDefinition</a></i>
</pre>

## Properties

#### Dependency

_Required_: No

_Type_: List of <a href="dependencydefinition.md">DependencyDefinition</a>

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

