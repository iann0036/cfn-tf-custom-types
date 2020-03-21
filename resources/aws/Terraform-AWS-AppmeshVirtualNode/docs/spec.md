# Terraform::AWS::AppmeshVirtualNode Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backends" title="Backends">Backends</a>" : <i>[ String, ... ]</i>,
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="spec-backend.md">Backend</a>, ... ]</i>,
    "<a href="#listener" title="Listener">Listener</a>" : <i>[ <a href="spec-listener.md">Listener</a>, ... ]</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="spec-logging.md">Logging</a>, ... ]</i>,
    "<a href="#servicediscovery" title="ServiceDiscovery">ServiceDiscovery</a>" : <i>[ <a href="spec-servicediscovery.md">ServiceDiscovery</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backends" title="Backends">Backends</a>: <i>
      - String</i>
<a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="spec-backend.md">Backend</a></i>
<a href="#listener" title="Listener">Listener</a>: <i>
      - <a href="spec-listener.md">Listener</a></i>
<a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="spec-logging.md">Logging</a></i>
<a href="#servicediscovery" title="ServiceDiscovery">ServiceDiscovery</a>: <i>
      - <a href="spec-servicediscovery.md">ServiceDiscovery</a></i>
</pre>

## Properties

#### Backends

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No
_Type_: List of <a href="spec-backend.md">Backend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No
_Type_: List of <a href="spec-listener.md">Listener</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No
_Type_: List of <a href="spec-logging.md">Logging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDiscovery

_Required_: No
_Type_: List of <a href="spec-servicediscovery.md">ServiceDiscovery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

