# Terraform::AWS::AppmeshVirtualNode Listener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="listener-healthcheck.md">HealthCheck</a>, ... ]</i>,
    "<a href="#portmapping" title="PortMapping">PortMapping</a>" : <i>[ <a href="listener-portmapping.md">PortMapping</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="listener-healthcheck.md">HealthCheck</a></i>
<a href="#portmapping" title="PortMapping">PortMapping</a>: <i>
      - <a href="listener-portmapping.md">PortMapping</a></i>
</pre>

## Properties

#### HealthCheck

_Required_: No
_Type_: List of <a href="listener-healthcheck.md">HealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMapping

_Required_: No
_Type_: List of <a href="listener-portmapping.md">PortMapping</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

