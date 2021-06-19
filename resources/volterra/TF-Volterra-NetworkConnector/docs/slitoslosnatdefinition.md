# TF::Volterra::NetworkConnector SliToSloSnatDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultgwsnat" title="DefaultGwSnat">DefaultGwSnat</a>" : <i>Boolean</i>,
    "<a href="#dynamicrouting" title="DynamicRouting">DynamicRouting</a>" : <i>Boolean</i>,
    "<a href="#interfaceip" title="InterfaceIp">InterfaceIp</a>" : <i>Boolean</i>,
    "<a href="#snatpool" title="SnatPool">SnatPool</a>" : <i>String</i>,
    "<a href="#snatpoolallocator" title="SnatPoolAllocator">SnatPoolAllocator</a>" : <i>[ <a href="snatpoolallocatordefinition.md">SnatPoolAllocatorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultgwsnat" title="DefaultGwSnat">DefaultGwSnat</a>: <i>Boolean</i>
<a href="#dynamicrouting" title="DynamicRouting">DynamicRouting</a>: <i>Boolean</i>
<a href="#interfaceip" title="InterfaceIp">InterfaceIp</a>: <i>Boolean</i>
<a href="#snatpool" title="SnatPool">SnatPool</a>: <i>String</i>
<a href="#snatpoolallocator" title="SnatPoolAllocator">SnatPoolAllocator</a>: <i>
      - <a href="snatpoolallocatordefinition.md">SnatPoolAllocatorDefinition</a></i>
</pre>

## Properties

#### DefaultGwSnat

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicRouting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatPool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatPoolAllocator

_Required_: No

_Type_: List of <a href="snatpoolallocatordefinition.md">SnatPoolAllocatorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

